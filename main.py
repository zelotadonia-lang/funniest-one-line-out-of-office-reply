#!/usr/bin/env python3
"""Write one original one-line out-of-office reply to /output/entry.txt."""

import os

JOKE = "I'm away. My auto-reply has been promoted to acting manager while I'm gone, and it already denied your request."
# Single line, 113 characters: inside the gate of 1 to 160 UTF-8 characters.


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
