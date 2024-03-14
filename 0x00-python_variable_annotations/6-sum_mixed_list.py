#!/usr/bin/env python3
"""
This is a module that provides a function which takes a list
of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the numbers in the mixed list as a float.
    """
    return sum(mxd_lst)
