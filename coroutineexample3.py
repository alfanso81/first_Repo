import asyncio
import threading

async def hello():
    print('Hello World! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello Again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
task = [hello(), hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()
