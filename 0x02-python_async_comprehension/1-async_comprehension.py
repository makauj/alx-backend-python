#!/usr/bin/env python3
"""async comprehension"""


import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Async comprehension"""
    comprehend = []
    async for i in async_generator():
        comprehend.append(i)
    return comprehend
