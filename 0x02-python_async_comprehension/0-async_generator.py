#!/usr/bin/env python3

""" This program creates a coroutine called async_generator"""

import asyncio
import random
import generator

async def async_generator() -> int:
    """
       args:
       nil arguments passed
       Return:
       it returns a random integer
    """
    for _ in range(10):
        await asyncio.sleep(1)
        return random.uniform(0, 10)
