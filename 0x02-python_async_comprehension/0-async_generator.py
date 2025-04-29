#!/usr/bin/python3
"""Task 0
"""
import asyncio
import random


async def async_generator():
    """
    Allows looping 10 times, each time asynchronously. Then return a number btn
    0 & 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
