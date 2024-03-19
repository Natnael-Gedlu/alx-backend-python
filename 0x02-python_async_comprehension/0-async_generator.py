#!/usr/bin/python3
"""
Module contains an asynchronous function that
yields a random float number between 0-10 for
10 iterations with one-second delay
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    asynchronous function that
    yields a random float number between 0-10 for
    10 iterations with one-second delay each
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
