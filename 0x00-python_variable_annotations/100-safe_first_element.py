#!/usr/bin/env python3
"""Augmented code with the correct duck-typed annotations."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the sequence
    if not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
