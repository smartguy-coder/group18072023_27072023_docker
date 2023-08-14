import asyncio


async def first():
    print('Executing first')
    result = 0
    for i in range(1, 11):
        print(f'Task 1: {i} step')
        result += i
        await asyncio.sleep(1)
    print(f'Task 1: {result=}')
    return result


async def second():
    print('Executing second')
    result = 1
    for i in range(1, 11):
        print(f'Task 2: {i} step')
        result *= i

        await asyncio.sleep(1)
    print(f'Task 2: {result=}')
    return result


async def callback():
    result1 = await first()
    result2 = await second()
    return result1, result2


event_loop = asyncio.get_event_loop()


try:
    value1, value2 = event_loop.run_until_complete(callback())
    print(value1, value2)
finally:
    event_loop.close()
