import os

SENTENCE = "Ma'am, I know the Wi-Fi died mid-meeting and the printer sounds possessed, but have you tried turning it off and on again? It's the IT version of a deep breath."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")

if __name__ == "__main__":
    main()
