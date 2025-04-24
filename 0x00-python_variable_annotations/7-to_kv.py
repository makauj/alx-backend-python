#!/usr/bin/env python3
"""to kv.py
"""
from typing import List, Tuple, Union


def to_kv(
    kvs: List[Tuple[str, Union[int, float]]]
) -> List[Tuple[str, Union[int, float]]]:
    """
    Returns a list of tuples with the first element as the key and the
    second element as the square of the value
    """
    return [(k, v * v) for k, v in kvs]
