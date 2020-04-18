import asyncio


class Filled:
    color = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ("red", "green", "blue"):
            raise ValueError("Fills need a valid color")


class Polygon:
    sides = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError("Polygons need 3+ sides")


class RedTriangle(Filled, Polygon):
    color = "red"
    sides = 4
    # color = "yellow" raise exception by Filled father class
    # sides = 2 raise exception by Polygon father class


async def main():
    ruddy = RedTriangle()

if __name__ == "__main__":
    asyncio.run(main())
