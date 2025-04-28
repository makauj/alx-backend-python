#!/usr/bin/env python3
"""more tasks"""


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random
from typing import List


async def task_wait_n(n: int, max_delay: int) -> float:
    """
    returns a asyncio.Task
    """
    tasks = []
    delays = []

    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
