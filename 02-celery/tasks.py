import time
import redis
from celery import Celery
from celery.decorators import periodic_task
from datetime import timedelta
from celery.task.schedules import crontab


# Celery let you configure several backends.
# One is memcache, that stores all your returned values in memory.
# Can use a DB as a backend.
# Can use redis itself
# And others...
# If we do not explicitely specify a backend, celery does not return result, it is just a queue.
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

########################################################

# This transforms a function into a celery task
@app.task(name='tasks.add')
def add(x, y):
	total = x + y
	print('{} + {} = {}'.format(x, y, total))
	# Simulate long running task
	time.sleep(5)
	return total

########################################################

"""Exception Handling keythings:
    * Gracefully handle exception in distributed workers
    * Leverage on error retris and exponential backoffs
    * Distributed workers should fail fast and should not block forever
"""

def backoff(attempts):
	"""
	1, 2, 4, 8, 16, 32...
	"""
	return 2 ** attempts


# bind: Make the first arg of the function, the task itself.
# soft time limit: If task does not end in the amount of seconds, it will raise the soft limit Exception.
@app.task(bind=True, max_retries=4, soft_time_limit=5)
def data_extractor(self):
    try:
        for i in range(1, 11):
            print('Crawling HMTL DOM!')
            if i == 5:
                raise ValueError('Crawling Index Error')
    except Exception as exc:
        print('There was an exception lets retry after X seconds')
        # It will retry after 5 seconds, and after 4 (max_retries) it will rasie the ValueError
        # raise self.retry(exc=exc, countdown=5)

        # This is an exponential retry seconds count. Every time it fails, we make
        # the task wait more to be re executed.
        secs = backoff(self.request.retries)
        raise self.retry(exc=exc, countdown=secs)

########################################################
# Simple periodic task

#@periodic_task(run_every=timedelta(seconds=3), name="tasks.send_mail_from_queue")
def send_mail_simple():
	try:
		messages_sent = "example.email"
		print("Email message successfully sent, [{}]".format(messages_sent))
	finally:

# With crontab, complex scheduling
#@periodic_task(run_every=(crontab(day_of_week='sunday', minute='*/1')), name="tasks.send_mail_in_queue_task", ignore_result=True)
def send_mail_simple2():
	try:
		messages_sent = "example.email"
		print("Total email message successfully sent %d.", messages_sent)
	finally:
		print("release resources")

	print("release resources")

########################################################
# Periodic task used for mutual exclusion

key = "4088587A2CAB44FD902D6D5C98CD2B17"

# We need to apply some kind of lock in the try/finally block.
@periodic_task(bind=True, run_every=timedelta(seconds=5), name="tasks.send_mail_from_queue")
def send_mail_from_queue(self):
    REDIS_CLIENT = redis.Redis()
    # lock will be automatically released after this time
    timeout = 60 * 5  # Lock expires in 5 minutes
    have_lock = False
    # key will be stored by redis and be used as a mutex, a global locking mutex
    my_lock = REDIS_CLIENT.lock(key, timeout=timeout)
    try:
        # Start of critical section
        have_lock = my_lock.acquire(blocking=False)
        if have_lock:
            messages_sent = "example.email"
            # self.request.hostname == name of the worker
            print("{} Email message successfully sent, [{}]".format(self.request.hostname, messages_sent))
            time.sleep(10)
    finally:
        print("release resources")
        if have_lock:
            my_lock.release()
