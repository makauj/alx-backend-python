#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """returns a random delay between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
# Example usage

if __name__ == "__main__":
    # Run the coroutine and print the result
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
    print(asyncio.run(wait_random(0)))
    print(asyncio.run(wait_random(100)))
    print(asyncio.run(wait_random(50)))
