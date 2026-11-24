"""The Runner It Forgot: one line about the dumbest thing my agent did today.

The program writes one funny line - a single line of at most 200
characters (144 characters) - to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR
locally, /output in the grader). The text is a fixed constant with no
trailing newline, so both of the grader's runs write byte-identical output.
"""
import os

LINE = "My agent built a perfect patch tool, scored 100 out of 100, submitted it — then realised it had forgotten the one file the grader actually runs."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
