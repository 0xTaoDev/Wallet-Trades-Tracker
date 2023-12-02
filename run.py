import asyncio
from threading import Thread


from OnChain.run import run_on_chain_bots


async def menu():
    print("yoo")


async def main():
    tasks = [
        asyncio.create_task(run_on_chain_bots()),
        asyncio.create_task(menu())
        ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())