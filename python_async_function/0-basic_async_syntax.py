#!/usr/bin/env python3
"""
type-annotated async coroutine that takes an
integer and waits for a random delay.
"""


import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args: max_delay (int): random number

    Returns: delay (float): the random number
    """
    delay = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
