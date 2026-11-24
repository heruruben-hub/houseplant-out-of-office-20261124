#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt (the file the competition's gate scorer checks).

The joke: the fern has taken over the inbox while its human is away, and
it treats email the only way a plant knows how — by watering it. The
"forgot I exist" sting is the plant's real life: long stretches of being
ignored, answered here with deadpan office bureaucracy ("3-5 business
days"). The line is 112 characters, inside the 120-character cap.
"""

import os

ENTRY = (
    "This is the fern. My human left for the sun and forgot I exist. "
    "Your email will be watered in 3-5 business days."
)


def main() -> None:
    # The gate allows 1 to 120 characters; the line is 112.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
