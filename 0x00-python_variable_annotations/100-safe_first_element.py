#!/usr/bin/env python3
"""
This module contains the safe_first_element function that retrieves
the first element of a sequence if it exists, or None if it doesn't.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely get the first element of a sequence.

    Parameters:
    - lst (Sequence[Any]): The sequence to get the first element from.

    Returns:
    - Union[Any, None]: The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
