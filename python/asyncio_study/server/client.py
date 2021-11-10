import asyncio

import aiohttp


async def some_unnecessary_wait():
    print("First sleep")
    await asyncio.sleep(1)
    print("Second sleep")
    await asyncio.sleep(1)
    print("Third sleep")
    await asyncio.sleep(1)
    print("Fourth sleep")
    await asyncio.sleep(1)


async def parse_web(session: aiohttp.ClientSession, url: str) -> str:
    print(f"Starting to parse the web with url {url}")
    async with session.get(url) as response:
        print(response.status)
        await some_unnecessary_wait()
        html = await response.text()
        print("Body:", html[:15], "...")
    print(f"Stopping to parse the web with url {url}")
    return html


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(
            parse_web(session, "http://0.0.0.0:8080"),
            parse_web(session, "http://0.0.0.0:8080/paul"),
            parse_web(session, "http://0.0.0.0:8080/kotja"),
            parse_web(session, "http://0.0.0.0:8080/alex"),
            parse_web(session, "http://0.0.0.0:8080/asdasd"),
            parse_web(session, "http://0.0.0.0:8080/qweqwe"),
        )
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
