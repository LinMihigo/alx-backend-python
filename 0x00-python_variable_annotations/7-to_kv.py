#!/usr/bin/env python3
"""
Module contains the to_kv function
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function that returns tuple of k and square of v

    Args:
        k: string value
        v: int/float value

    Returns:
       Tuple of k and square of v
    """
    return (k, v**2)
