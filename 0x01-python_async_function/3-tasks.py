#!/usr/bin/env python3
"""Tasks"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns a asyncio.Task
    Args:
        max_delay (int): maximum delay
    Returns:
        float: delay
    """
    return asyncio.create_task(wait_random(max_delay))
