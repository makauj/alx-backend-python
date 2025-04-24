#!/usr/bin/env python3
"""
element length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with the first element as the input
    and the second element as the length of the input
    """
    return [(i, len(i)) for i in lst]
