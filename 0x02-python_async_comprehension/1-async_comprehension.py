#!/usr/bin/env python3
"""Task 1
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random no. using async comprehensing over
    async_generator
    """
    return [i async for i in async_generator()]
