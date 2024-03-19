#!/usr/bin/env python3
"""
Module contains an asynchronous comprehension function,
async_comprehension,which asynchronously generates a
list of floating-point numbers using an async generator.
"""
from importlib import import_module as using
from typing import List
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously generates a list of
    floating-point numbers using an async generator.
    """
    return [num async for num in async_generator()]
