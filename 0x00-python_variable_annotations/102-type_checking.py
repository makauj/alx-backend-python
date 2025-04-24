#!/usr/bin/env python3
"""type checking for the 'pydantic' library"""
from typing import


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in or out on a list of integers by a given factor."""
    zoomed: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed


array = (12, 72, 91)

zoom_2x = zoom_array(arr)

zoom_3x = zoom_array(array, 3)
