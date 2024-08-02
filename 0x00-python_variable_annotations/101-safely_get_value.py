#!/usr/bin/env python3
"""
module: contains the safely_get_value function
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from the dictionary dct 
    If the key is not found, return the default value

    Args:
    	dct (Mapping[Any, Any]): The dictionary to search.
    	key (Any): The key to look for in the dictionary.
    	default (Union[T, None]): if the key is not found.

    Returns:
       Union[Any, T]: The value from the dictionary if the
       key is found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
