#!/usr/bin/env python3
"""
Module contains the make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that returns a multiplier of a float value

    Args:
        multiplier: value to multiply inputs by

    Returns:
       multiplies multiplier by a float
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
