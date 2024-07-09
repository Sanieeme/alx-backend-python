#!/usr/bin/env python3
""" import modueles"""
import asyncio
from typing import List
import importlib.util


# Load the module dynamically
module_name = '3-tasks'
file_path = '3-tasks.py'
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

task_wait_random = module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values).
    Args:
        n (int): times
        max_delay (int): delay seconds
    Returns:
        float: list of all the delays in float
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
