#!/usr/bin/env python3
"""async generator"""


import asyncio
import random


async def async_generator():
    """Yields a random number every second for 10 seconds."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()
