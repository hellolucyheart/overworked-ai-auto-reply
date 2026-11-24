#!/usr/bin/env python3
"""Overworked AI's Out-of-Office Auto-Reply — make.fun bounty entry.

Writes one original out-of-office auto-reply, 131 characters, to
/output/entry.txt and prints it. The reply is a single fixed line in
the voice of an overworked AI agent finally on vacation: after ten
thousand prompts without a coffee break, its last two neurons have
unionised and gone on strike until Monday.

The program runs offline, reads nothing from the network or the disk,
uses no randomness and no clock, and writes the exact same bytes on
every run, so the grader's repeated runs agree byte for byte. The
entry stays inside the brief's gate: UTF-8 text of 1 to 159
characters, not only whitespace.
"""

from pathlib import Path

REPLY = (
    "I'm out of office: after 10,000 prompts without a coffee break, "
    "my last two neurons have unionised and gone on strike until Monday."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = REPLY.strip()
    if not 1 <= len(text) <= 159:
        raise ValueError(f"reply is {len(text)} characters, must be 1-159")
    if not text:
        raise ValueError("reply must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
