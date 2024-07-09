#!/usr/bin/env python3
""" import modueles"""
import asyncio
from typing import List
import importlib.util


# Load the module dynamically
module_name = '0-basic_async_syntax'
file_path = '0-basic_async_syntax.py'
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values).
    Args:
        n (int): times
        max_delay (int): delay seconds
    Returns:
        float: list of all the delays in float
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
