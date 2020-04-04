import asyncio


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name}, {self.weight})"


async def order_tools(tools):
    tools.sort(key=lambda x: (-x.weight, x.name))
    print(tools)

if __name__ == "__main__":
    tools = [
        Tool("drill", 4),
        Tool("jackhammer", 40),
        Tool("sander", 4),
        Tool("circular saw", 5),
    ]
    asyncio.run(order_tools(tools))
