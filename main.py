#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes exactly one roast line to /output/entry.txt.

The line is a single deadpan roast aimed at the smart fridge itself:
its door alarm screams over five seconds of open door, yet it stays
silent about leftovers that have been decomposing since March.
One absurd concrete incident, named once, no explanation.
"""

ROAST = (
    "My fridge beeps if the door is open five seconds, "
    "yet says nothing about the leftovers decomposing since March."
)


def main() -> None:
    """Write the roast line to /output/entry.txt, one line, UTF-8."""
    import os

    # Gate check, same rule the sealed scorer applies: 1-200 chars,
    # not only whitespace, single line, valid UTF-8.
    line = ROAST.strip()
    assert line and len(line) <= 200, "roast line fails the gate"
    assert "\n" not in line, "roast line must be a single line"
    line.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
