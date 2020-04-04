import asyncio


async def good_code(names, counts):
    for name, count in zip(names, counts):
        print(f"{name}: {count}")

if __name__ == "__main__":
    names = ["Lise", "Marie", "Cecilia"]
    counts = [len(name) for name in names]
    asyncio.run(good_code(names, counts))
