#!/usr/bin/env python3
"""
module contains element_length function
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with elements and their lengths.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of (string, length) tuples.
    """
    return [(i, len(i)) for i in lst]
