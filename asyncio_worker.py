import aiofiles
import asyncio
from process_file import replace_symbol


async def process_file(filename):
    async with aiofiles.open(filename, 'r+') as f:
        content = await f.read()
        text = replace_symbol(content)
        await f.seek(0)
        await f.write(''.join(text))
        print(filename)


async def main_asyncio():
    await asyncio.gather(*[process_file(f"{i}.txt") for i in range(1, 11)])
    for j in range(11, 100, 10):
        await asyncio.gather(*[process_file(f"{i}.txt") for i in range(j, j+10)])


def start_asyncio():
    print("asyncio")
    asyncio.run(main_asyncio())
