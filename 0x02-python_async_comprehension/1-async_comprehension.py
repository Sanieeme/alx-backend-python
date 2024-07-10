#!/usr/bin/env python3
"""import modules"""
import importlib.util
import asyncio
from typing import List

module_name = '0-async_generator'
file_path = '0-async_generator.py'
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
async_generator = module.async_generator


async def async_comprehension() -> List[float]:
    """
    async comprehension
    Args:
        None
    Return:
    """
    result = [i async for i in async_generator()]
    return result
