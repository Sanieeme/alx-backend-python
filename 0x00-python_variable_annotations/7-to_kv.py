#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple

    Args:
        k (str): The input string.
        v (Union[int, float]): The numeric value.

    Returns:
        Tuple[str, float]: A tuple containing `k` and the square of `v`.
    """
    return (k, float(v ** 2))
