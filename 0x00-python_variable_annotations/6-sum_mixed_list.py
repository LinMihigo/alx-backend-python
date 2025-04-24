#!/usr/bin/env python3
"""
Module contains the sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, str]]) -> float:
    """
    function that returns the sum of int and float values in a list

    Args:
        mxd_lst: list

    Returns:
       sum of int and float values in a list
    """
    return float(sum(mxd_lst))
