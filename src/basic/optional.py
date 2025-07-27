"""
foo can accept an integer argument, None or no argument at all.
"""
from typing import Optional

def foo(x: int | None = 0):
    pass

## End of your code ##
foo(10)
foo(None)
foo()

foo("10")  # expect-type-error