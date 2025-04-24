#!/usr/bin/env python3
"""
2-floor.py
"""


def floor(n: float) -> int:
    """
    Returns the floor of a number
    """
    if n >= 0:
        return int(n)
    return int(n) - 1
