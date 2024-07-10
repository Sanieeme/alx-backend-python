#!/usr/bin/env python3
"""import module"""
import importlib.util
import time
import asyncio


# Load the module dynamically
module_name = '1-async_comprehension'
file_path = '1-async_comprehension.py'
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

async_comprehension = module.async_comprehension


async def measure_runtime():
    """
    measure the total runtime
    Args:
        None
    Returns:
         total runtime
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
