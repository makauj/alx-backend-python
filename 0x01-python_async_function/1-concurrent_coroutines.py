#!/usr/bin/env python3
"""Concurrency coroutines"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function
    Args:
        n (int): number of times to wait
        max_delay (int): maximum delay
    Returns:
        list: sorted list of delays
    """
    tasks = []
    delays = []

    for i in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
