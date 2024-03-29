import time
import threading

"""
When we execute this we will see that the print at the end is executed almost at the
beggining, and the counters are executed concurrently
"""

def countdown(count):
	while(count >= 0):
		print("{} Counting down buddy! {}".format(threading.current_thread().name, count))
		count -= 1
		time.sleep(3)


def countup(count):
	while(count <= 10):
		print("{} Counting up buddy! {}".format(threading.current_thread().name, count))
		count += 1
		time.sleep(5)


t1 = threading.Thread(name="countdown", args=(10,), target=countdown)
t1.start()

t2 = threading.Thread(name="countup", args=(0,), target=countup)
t2.start()

print("All done!")
