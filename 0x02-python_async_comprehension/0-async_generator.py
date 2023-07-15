#!/usr/bin/env python3

""" This program creates a coroutine called async_generator"""

import asyncio
import random
from typing import generator

async def async_generator() -> [float, None, None]:
    """
       args:
       nil arguments passed
       Return:
       it returns a random integer
    """
    a = 0
    while (a < 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
