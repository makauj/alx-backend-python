#!/usr/bin/env python3
"""Measure runtime"""


import time
import asyncio
from typing import Callable, Any
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of an async comprehension
    Args:
        async_comprehension (Callable[[], Any]):
        The async comprehension to measure.
    Returns:
        float: The total runtime of the async comprehension.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return (end_time - start_time)
