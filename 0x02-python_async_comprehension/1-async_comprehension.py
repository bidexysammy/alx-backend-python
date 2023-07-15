#!/usr/bin/env python3

""" 
    This program uses comprehension to get list of random numbers
"""

import typing

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List(float):
    """
       args:
       no argument is passed
       Returns:
       returns 10 random numbers
    """
    return(i async for i in async_generator())
        
