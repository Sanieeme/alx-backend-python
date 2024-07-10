#!/usr/bin/env python3
"""corouutine function"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
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
