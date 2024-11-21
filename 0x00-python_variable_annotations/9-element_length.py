#!/usr/bin/env python3
"""
A function with annotated parameters and
return values with appropriate types.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with the element and its length."""
    return [(i, len(i)) for i in lst]
