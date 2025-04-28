#!/usr/bin/env python3
"""more tasks"""


from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random



async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns a asyncio.Task
    """
    tasks = []
    delays = []

    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
