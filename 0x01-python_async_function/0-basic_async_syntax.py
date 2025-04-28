#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import random
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> int:
    """returns a random delay between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await sleep(delay)
    return int(delay)
