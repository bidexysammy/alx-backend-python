#!/usr/bin/env python3

"""
This module takes an integer number and returns it eventually after some seconds
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
	"""
	args:
	The argument is max_delay.
	returns:
	random number generated.
	"""
	x: float = random.uniform(0, max_delay)
	await asyncio.sleep(x)
	return x
