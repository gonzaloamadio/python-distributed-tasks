import threading

import time
import random
import atexit

queue = []
MAX_ITEMS = 10

# A factory function that returns a new condition variable object.
#A condition variable allows one or more threds to wait until they are notified by another thread
condition = threading.Condition()


class ProducerThread(threading.Thread):

	def run(self):

		numbers = range(5)
		global queue

		while True:
			condition.acquire()
			if len(queue) == MAX_ITEMS:
				print("Queue is full, producer is waiting")
				# condition variables allows one or more threads to wait until they
				# are notified by anothe thread.
				# Wait blocks this thread and also release the lock associated with the condition
				# So basically here producer will lose the hold of the lock.
				# But unless producer is notified it will not run, and consumer can acquire the lock
				# because it was released
				condition.wait()
				print("Space in queue, Consumer notified producer")
			number = random.choice(numbers)
			queue.append(number)
			print("Produced {}".format(number))
			# Notify does not release the lock.
			condition.notify()
			condition.release()
			time.sleep(random.random())


class ConsumerThread(threading.Thread):

	def run(self):
		global queue
		while True:
			condition.acquire()
			if not queue:
				print("Nothing in queue, consumer is waiting")
				condition.wait()
				print ("Producer added something to queue and notify the consumer")

			number = queue.pop(0)
			print("Consumed {}".format(number))
			condition.notify()
			condition.release()
			time.sleep(random.random())


producer = ProducerThread()
# If not, thread will never terminate
producer.daemon = True
producer.start()

consumer = ConsumerThread()
consumer.daemon = True
consumer.start()


def exit_handler():
	# refer to https://docs.python.org/3/library/atexit.html
	print("Terminating producer, consumer, mainApp...")


atexit.register(exit_handler)

# we make the main thread to never terminate unless we do that.
# So whenever we kill the main thread, then also the daeminzed threads end altogether
while True:
	time.sleep(1)
