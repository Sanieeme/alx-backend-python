#!/usr/bin/env python3
"""function`s parameter"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return values with the appropriate types
    Args:
        lst(iterable[sequence]): iterable sequence
    Returns:
        list
    """
    return [(i, len(i)) for i in lst]
