import asyncio
from functools import wraps
from aiocache import cached


def trace(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        print(f"{func.__name__}({args!r}), ({kwargs!r})"
              f" -> {result!r}")
        return result
    return wrapper


@trace
@cached()
async def fibonacci(n):
    if n in (0, 1):
        return n
    return await fibonacci(n - 2) + await fibonacci(n - 1)


if __name__ == "__main__":
    try:
        result = asyncio.run(fibonacci(4)) 
        print(result)
    except Exception as error:
        print(f"fibonacci() error -> {error}")