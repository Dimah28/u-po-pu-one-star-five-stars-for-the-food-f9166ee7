#!/usr/bin/env python3
"""Write a one-star review of Earth by an alien tourist that still
compliments the food.

Deterministic, stdlib only, no network. Writes /output/entry.txt.

The review (168 characters, one sentence): an alien tourist complains
that Earth's gravity bruised a third knee, the weather changed four
times before lunch, and nobody apologized -- then admits the street
noodles were worth crash-landing for. The turn from grievance to
compliment is the joke: the food alone justifies the trip.
"""

import os

ENTRY = (
    "One star: your gravity bruised my third knee, your weather changed "
    "four times before lunch, and nobody apologized \u2014 but the street "
    "noodles were worth crash-landing for."
)


def validate_entry(text: str) -> None:
    """Gate: one line of UTF-8 text, 1-200 characters, not only whitespace."""
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("entry must be 1-200 characters, not only whitespace")
    if "\n" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
