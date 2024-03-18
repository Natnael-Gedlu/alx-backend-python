#!/usr/bin/env python3
"""
Module that contains Asynchronously spawns wait_random n
times with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random n times with the specified max_delay.
    """
    delays = []
    x = []

    for i in range(n):
        task = wait_random(max_delay)  # Spawn a new task
        x.append(task)

    for task in asyncio.as_completed(x):  # Iterate over x, not p
        delay = await task
        delays.append(delay)

    return delays
