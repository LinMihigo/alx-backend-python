#!/usr/bin/env python3
"""Task 0
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay btn 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
