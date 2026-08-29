#!/usr/bin/env python3
"""
type-annotated async coroutine that takes an
integer and waits for a random delay.
"""


import asyncio, random


async def wait_random(max_delay: int = 10) -> int:
    """
    Args: max_delay (int): random number

    Returns: int: the random number
    """
    await asyncio.sleep((random.uniform(0, float(max_delay))))
    return max_delay
