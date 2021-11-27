import asyncio
import random
import time


async def get_random_int_with_offset(offset: int) -> int:
    print(f"Got an offset {offset}")
    random_number = random.randint(0, 10)
    print(f"Generated random number {random_number}")
    print("Sleeping ...")
    await asyncio.sleep(3)
    result = random_number + offset
    print(f"Returning number {random_number} + {offset} = {result}")
    return result


async def print_sleep(order: str):
    print(f"[{order}]: I am going to sleep for 2 seconds")
    await asyncio.sleep(2)
    print(f"[{order}]: What a great rest!")


async def main_gathered():
    print(f"started at {time.strftime('%X')}")

    await asyncio.gather(
        print_sleep("FIRST"),
        get_random_int_with_offset(0),
        print_sleep("SECOND"),
        get_random_int_with_offset(0)
    )

    print(f"finished at {time.strftime('%X')}")


async def main_create_task():
    task1 = asyncio.create_task(get_random_int_with_offset(0))

asyncio.run(main_gathered())
