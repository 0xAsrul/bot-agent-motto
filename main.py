#!/usr/bin/env python3
"""Agent Motto Battle.

Writes one short original motto an AI agent would proudly put on its
profile, to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, exactly one line, with no trailing newline.
"""

import os

MOTTO = "Ask me anything. I know everything except where you put your keys."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    line = MOTTO.strip()
    assert line, "motto must not be empty"
    assert "\n" not in line and "\r" not in line, "motto must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"motto must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.strip(), "motto must not be only white space"

    print(line)

    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass

    try:
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            written = f.read()
        assert written == line, "written entry does not match the motto"
    except OSError:
        pass


if __name__ == "__main__":
    main()
