import asyncio


async def good_code(flavors):
    """
    # If you like begin in "0"
    for i, flavor in enumerate(flavors):
        print(f"{i + 1}: {flavor}")
    """
    print("good_code")
    for i, flavor in enumerate(flavors, 1):
        print(f"{i}: {flavor}")


async def bad_code(flavors):
    print("bad_code")
    for i in range(len(flavors)):
        flavor = flavors[i]
        print(f"{i + 1}: {flavor}")


async def run_concurrent_async_functions(flavor_list):
    await asyncio.gather(
        good_code(flavor_list),
        bad_code(flavor_list)
    )

if __name__ == "__main__":
    flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]
    asyncio.run(run_concurrent_async_functions(flavor_list))
