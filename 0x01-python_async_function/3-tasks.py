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


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    takes an integer
    Args:
        max_delay (int): delay in seconds
    Returns:
        asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
