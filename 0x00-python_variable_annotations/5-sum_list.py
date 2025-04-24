#!/usr/bin/env python3
"""
6-sum_list.py
This module contains a function that sums all the floats in a list.
"""


from typing import List


def sum_list(input_list: List(float)) -> float:
    """
    Sum all the floats in a list.
    Args:
        input_list (list): A list of floats.
    Returns:
        int: The sum of all floats in the list.
    """
    return float(sum(input_list))
