#!/usr/bin/env python3
"""
This is a module that provides a function that takes list of
floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)
