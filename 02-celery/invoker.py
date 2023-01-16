import time
from tasks import add, data_extractor
from celery.result import AsyncResult


###################################
# Sum function
###################################

# This will create the producer, invoke the celery task
result = add.delay(1, 2)

print(result) # this will print the task id

# Blocker, will wait until result is present
#print("result.get(): {}".format(result.get()))

while True:
    print("into loop")
    # If we want the actual result, we need to
    _result2 = AsyncResult(result.task_id)
    status = _result2.status
    print(status)
    if 'SUCCESS' in status:
        print('result after wait {_result2}'.format(_result2=_result2.get()))
        break
    time.sleep(3)


###################################
# Crawl html function
###################################

data_extractor.delay()

###################################
# Send mail, periodic task call
###################################


