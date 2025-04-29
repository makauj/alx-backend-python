#!/usr/bin/env python3
"""async comprehension"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension
    Yields 10 random numbers between 0 and 10.
    Returns:
        list: A list of 10 random numbers.
    """
    comprehend = []
    async for i in async_generator():
        comprehend.append(i)
    return comprehend
