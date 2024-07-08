#!/usr/bin/env python3
"""Asynchronous coroutine."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument.

    Args:
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
