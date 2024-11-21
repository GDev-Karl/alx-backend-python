#!/usr/bin/env python3
from typing import List

"""
A type-annotated function sum_list which
takes a list input_list of floats as argument
and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    Takes a list of floats and returns their sum as a float.

    Args:
        input_list (List[float]): List of floating-point numbers.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
