import asyncio
import time

async def myWork():
    print("Starting Work")
    time.sleep(5)
    print("Finishing Work")

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(myWork())
finally:
    loop.close()