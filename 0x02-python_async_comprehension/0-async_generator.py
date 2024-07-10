#!/usr/bin/env python3
"""corouutine function"""
import random
import asyncio


async def async_generator() -> float:
    """
    takes no arguments
    Args:
        None
    Returns:
        print random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
