import aiofiles
import asyncio


async def process_file(filename):
    async with aiofiles.open(filename, 'r+') as f:
        content = await f.read()
        text = list(content)
        for i in range(len(text)):
            if (i+1)%5==0:
                text[i] = "*"
        await f.seek(0)
        await f.write(''.join(text))


async def main():
    await asyncio.gather(*[process_file(f"{i}.txt") for i in range(1, 11)])
    for j in range(11, 100, 10):
        await asyncio.gather(*[process_file(f"{i}.txt") for i in range(j, j+10)])


def start():
    print("asyncio")
    asyncio.run(main())