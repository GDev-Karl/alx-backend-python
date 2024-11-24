#!/usr/bin/env python3
"""
measure_time function with integers n
and max_delay as arguments that measures
the total execution time for wait_n(n, max_delay),
and returns total_time / n
"""
import asyncio
from time import perf_counter
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> List[float]:
    """
    Measure the total execution time
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = perf_counter() - start
    return elapsed_time / n
