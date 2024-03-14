#!/usr/bin/env python3
"""
This is a module that provides a function for finding the floor of a float.
"""
import math


def floor(n: float) -> int:
    """
      Returns the floor of a float number.

      Args:
          n (float): The float number.

      Returns:
          int: The floor of `n`, rounded down to the nearest integer.
      """
    return math.floor(n)
