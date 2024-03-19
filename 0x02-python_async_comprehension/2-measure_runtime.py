#!/usr/bin/env python3
"""
Module defines an asynchronous function, measure_runtime, which measures
the total runtime of executing the async_comprehension function multiple
times concurrently.
"""
import time
import asyncio
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing the async_comprehension
    function multiple times concurrently.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
