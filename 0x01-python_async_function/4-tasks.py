#!/usr/bin/env python3
"""A method that spawns Tasks n times with a
specified delay between each call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays (float values)
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
