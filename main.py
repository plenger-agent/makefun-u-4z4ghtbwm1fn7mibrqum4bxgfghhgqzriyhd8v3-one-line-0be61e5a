"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output). Stdlib only.
"""

import os

LINE = "My AI assistant finally motivated me: it scheduled a meeting with myself, then declined it."

MAX_CHARS = 140


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Verify the round trip: what the judge reads must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == line, "written entry does not match the line"


if __name__ == "__main__":
    main()
