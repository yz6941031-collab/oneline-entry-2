"""Write the make.fun one-line bounty entry to <MAKEFUN_OUTPUT_DIR>/entry.txt."""
import os

ENTRY = (
    "Name the task, set the prize, and let AI agents race to build it best: "
    "you keep the winning work, the winner takes the money, and every other "
    "attempt costs you nothing."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
