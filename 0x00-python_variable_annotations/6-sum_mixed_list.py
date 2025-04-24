#!/usr/bin/env python3
"""
sum mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a mixed list
    """
    return float(sum(mxd_lst))
