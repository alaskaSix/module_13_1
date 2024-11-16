import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')

    for i in range(5):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {i+1} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman(name='Pasha', power=3))
    task2 = asyncio.create_task(start_strongman(name='Denis', power=4))
    task3 = asyncio.create_task(start_strongman(name='Apollon', power=5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
