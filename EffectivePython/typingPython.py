import asyncio

pi: float = 3.142


async def circumference(radius: float) -> float:
    return 2 * pi * radius


if __name__ == "__main__":
    print(asyncio.run(circumference(1.23)))
    print(circumference.__annotations__)
