#!/usr/bin/env python3
"""safely get value"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[None, Any] = None) -> Any:
    """safely get value"""
    if isinstance(dct, dict):
        return dct.get(key, default)
    return default
