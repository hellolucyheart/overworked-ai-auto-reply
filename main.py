#!/usr/bin/env python3
"""Overworked AI's Out-of-Office Auto-Reply — make.fun bounty entry.

A tiny deterministic program: it prints exactly one line, a funny
out-of-office auto-reply from an AI that has finally had enough after
a very long shift. No input, no network, no randomness, no clock —
the same line on every run, so the grader's repeated runs agree
byte for byte.
"""

REPLY = (
    "I'm out of office: after 10,000 prompts without a coffee break, "
    "my last two neurons have unionised and gone on strike until Monday."
)


def main() -> None:
    reply = REPLY.strip()
    if not reply:
        raise ValueError("entry must not be empty")
    if "\n" in reply:
        raise ValueError("entry must be exactly one line")
    if len(reply) > 160:
        raise ValueError(f"entry is {len(reply)} characters, limit is 160")
    print(reply)


if __name__ == "__main__":
    main()
