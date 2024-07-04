#!/usr/bin/env python3
""" type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier

    Args:
        multiplier(float): argument
    Return:
        float: multiplies
    """
    def multiply(x: float) -> float:
        return x * multiplier
    
    return multiply
