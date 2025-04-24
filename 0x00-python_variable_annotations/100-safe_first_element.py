#!/usr/bin/env python3
"""safe first element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a sequence or None"""
    if lst:
        return lst[0]
    return None
