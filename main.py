"""Funniest Autocorrect Fail entry.

Writes a single line -- one hilarious autocorrect fail, under 200
characters -- to /output/entry.txt, where the make.fun judge compares
it against other entries two at a time and picks the funnier one.

The line is a text to a colleague the morning before a big meeting:
one word slipped, and the intended word ("public") is obvious from
context, which is what makes it read as a real autocorrect fail
rather than a written joke.
"""

import os

ENTRY = (
    "I have to give a pubic presentation in front of the whole "
    "company tomorrow, wish me luck!"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def main() -> None:
    line = ENTRY.strip()
    # The sealed gate: UTF-8 text of 1 to 199 characters, not only
    # whitespace, a single line. Fail loudly here rather than
    # shipping an invalid entry.
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit("entry is over 199 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the line, so the
    # judge reads precisely what is shown above.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
