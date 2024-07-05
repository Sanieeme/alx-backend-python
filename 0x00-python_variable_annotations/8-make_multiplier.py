#!/usr/bin/env python3
""" type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value by which the returned function will multiply its input.

    Returns:
        Callable[[float], float]: A function that takes a float argument and returns the multiplied result.
    """
    def multiply(x: float) -> float:
        """
        Multiply the given float by the multiplier.

        Args:
            x (float): The float value to be multiplied.

        Returns:
            float: The result of x multiplied by multiplier.
        """
        return x * multiplier
    
    return multiply
