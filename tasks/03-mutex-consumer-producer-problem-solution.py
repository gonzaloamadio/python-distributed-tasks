import threading

# This global buffer will act as the shared resource
counter_buffer = 0
counter_lock = threading.Lock()

COUNTER_MAX = 1000000


def consumer1_counter():
	global counter_buffer
	for i in range(COUNTER_MAX):
	    # Between the acquire and release will be the critical code section
	    # i.e. the code that touch the shared resources.
		counter_lock.acquire()
		counter_buffer += 1
		counter_lock.release()


def consumer2_counter():
	global counter_buffer
	for i in range(COUNTER_MAX):
		counter_lock.acquire()
		counter_buffer += 1
		counter_lock.release()


t1 = threading.Thread(target=consumer1_counter)
t2 = threading.Thread(target=consumer2_counter)


t1.start()
t2.start()

# We need to join the main thread, that is the script itself
# or the beggining of the script with the imports, variables etc.
# And then we created other 2 threads t1, t2.
# With these joins we tell the main thread not to complete until
# t1 and t2 finish.
t1.join()
t2.join()

print(counter_buffer)


# NOTE: Try executing the script with the acquire and release commented out.
# You will see the result is not 2 millions anymore.
