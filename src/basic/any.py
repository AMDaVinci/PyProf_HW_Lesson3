from typing import Any

"""
Modify `foo` so it takes an argument of arbitrary type.
"""


def foo(x: Any):
    """⬆️ Change me. No need to implement the function."""


foo(1)
foo("10")
foo(1, 2)  # expect-type-error