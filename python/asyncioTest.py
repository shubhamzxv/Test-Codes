import asyncio
import time

def func1(a, b):
    time.sleep(1)
    print("Function 1 completed")
    return a+b

def func2(a, b):
    time.sleep(2)
    print("Function 2 completed")
    return a+b

def func3(a, b):
    time.sleep(3)
    print("Function 3 completed")
    return a+b

async def main():

    tasks =  [
        asyncio.create_task(asyncio.to_thread(func1,1,2)),
        asyncio.create_task(asyncio.to_thread(func2,2,3)),
        asyncio.create_task(asyncio.to_thread(func3,3,4))
    ]
    return await asyncio.gather(*tasks)


result = asyncio.run(main())
print(result)
