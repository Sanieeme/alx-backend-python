#!/usr/bin/env python3
"""corouutine function"""
import random
import asyncio


async def async_generator():
    """
    takes no arguments
    Args:
        None
    Returns:
        print random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
