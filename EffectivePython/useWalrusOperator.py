import asyncio


async def make_limonade(fresh_fruit):
    if (count := fresh_fruit.get("banana", 0)) >= 2:
        print(f"make_limonade {count}")


async def make_cider(fresh_fruit):
    if (count := fresh_fruit.get("apple", 0)) >= 4:
        print(f"make_cider {count}")


async def make_smoothies(fresh_fruit):
    if count := fresh_fruit.get("lemon", 0):
        print(f"make_smoothies {count}")


async def main(fresh_fruit):
    await asyncio.gather(
        make_limonade(fresh_fruit),
        make_cider(fresh_fruit),
        make_smoothies(fresh_fruit),
    )


if __name__ == "__main__":
    fresh_fruit = {
        "apple": 10,
        "banana": 3,
        "lemon": 5,
    }
    asyncio.run(main(fresh_fruit))
