"""
Change encoding.

Originally generated by Microsoft Copilot @ 2025-06-08.
"""

from pathlib import Path

source_dir_name = "mecab-naist-jdic-0.6.3b-20111013"
source_dir = Path(".") / source_dir_name
dest_dir = Path(".") / f"{source_dir_name}-UTF8"

# Ensure the destination directory exists
dest_dir.mkdir(parents=True, exist_ok=True)

# Process each file in the source directory
for source_path in source_dir.iterdir():
    if source_path.is_file():  # Ensure it's a file, not a directory
        dest_path = dest_dir / source_path.name

        # Read with EUC-JP encoding and write with UTF-8 encoding
        with source_path.open("r", encoding="euc-jp", errors="ignore") as infile, \
             dest_path.open("w", encoding="utf-8") as outfile:
            for line in infile:
                outfile.write(line)
