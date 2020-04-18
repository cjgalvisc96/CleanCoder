async def two():
    return 2


async def four():
    return await two() + await two()


async def eight():
    return await four() + await four()

def coro_manager(coro):
    try:
        coro.send(None)
    except StopIteration as stop:
        return stop.value

print(coro_manager(eight()))