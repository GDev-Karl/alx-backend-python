#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer
argument  named wait_random that waits for a random
delay between 0 and max_delay seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    Args:
        max_delay: The maximum delay to return
    Returns:
        A random float between 0 and max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
