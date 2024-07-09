#!/usr/bin/env python3
""" function with integers"""
import time
import importlib.util
import asyncio

# Load the module dynamically
module_name = '1-concurrent_coroutines'
file_path = '1-concurrent_coroutines.py'
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function with integers
    Args:
        n(int): time
        max_delay(int): delay
    Returns:
        float: returns a float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
