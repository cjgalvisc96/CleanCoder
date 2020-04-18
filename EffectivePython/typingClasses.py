import random
import asyncio
from typing import List, Tuple


SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


Card = Tuple[str, str]
Deck = List[Card]


async def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


async def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


async def choose(items):
    """Choose and return a random item"""
    return random.choice(items)


async def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = await choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]


async def play() -> None:
    """Play a 4-player card game"""
    deck = await create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, await deal_hands(deck))}
    start_player = await choose(names)
    turn_order = await player_order(names, start=start_player)
    # Randomly play cards from each player's hand until empty
    while hands[start_player]:
        for name in turn_order:
            card = await choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        print()


if __name__ == "__main__":
    asyncio.run(play())