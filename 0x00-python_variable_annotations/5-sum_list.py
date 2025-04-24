#!/usr/bin/env python3
"""
Module contains the sum_list function 
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function that returns the sum of float values in a list

    Args:
        input_list: list

    Returns:
       sum of float values in a list
    """
    return sum(input_list)
