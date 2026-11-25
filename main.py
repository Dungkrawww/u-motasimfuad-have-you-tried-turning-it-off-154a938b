# u-motasimfuad-have-you-tried-turning-it-off-154a938b: Have You Tried Turning It Off?
# One funny line, under 200 characters, that a hopeless tech support agent
# says to a desperate customer. The program writes the line to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-199 characters.
MAX_CHARS = 199

# The joke twists the classic instead of repeating it: the agent earnestly
# suggests apologising to the computer while it restarts, as if the machine
# had feelings and the agent believed it. The humour is the agent's cheerful
# uselessness; the customer is never the butt of it.
LINE = "Have you tried turning it off and on again \u2014 and while it restarts, maybe apologize to it? It looked upset."


def validate_line(line):
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars, must be 1-{MAX_CHARS}"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single line"


def main():
    validate_line(LINE)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
