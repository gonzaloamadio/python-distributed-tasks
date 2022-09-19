import time


def countdown(count):
	while(count >= 0):
		print("Counting down buddy! {}".format(count))
		count -= 1
		time.sleep(5)


# The print will not execute until cowntdown has finished
countdown(10)
print("All done!")
