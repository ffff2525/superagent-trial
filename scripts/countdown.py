#!/usr/bin/env python3
"""Count down from a positive integer and announce liftoff.

Usage::

    python scripts/countdown.py 3

prints ``3``, ``2``, ``1``, then ``Liftoff!``.  Invalid input (anything that
is not a positive integer) makes the script exit with status code 2.
"""

from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence


def positive_int(value: str) -> int:
    """argparse type: accept only positive integers.

    Raises ``argparse.ArgumentTypeError`` for anything that is not a
    positive integer, which makes argparse exit with status code 2.
    """
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"invalid positive integer: {value!r}"
        ) from None
    if number <= 0:
        raise argparse.ArgumentTypeError(
            f"expected a positive integer, got {value!r}"
        )
    return number


def build_parser() -> argparse.ArgumentParser:
    """Build the command line parser."""
    parser = argparse.ArgumentParser(
        prog="countdown.py",
        description="Count down from N to 1 and print 'Liftoff!'.",
    )
    parser.add_argument(
        "n",
        metavar="N",
        type=positive_int,
        help="starting number; must be a positive integer",
    )
    return parser


def countdown(n: int) -> None:
    """Print ``n`` down to ``1``, one number per line, then ``Liftoff!``."""
    for number in range(n, 0, -1):
        print(number)
    print("Liftoff!")


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the countdown script and return its exit status."""
    parser = build_parser()
    args = parser.parse_args(argv)
    countdown(args.n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
