#!/usr/bin/env python3
"""文本对比工具"""

import argparse
import difflib


def text_diff(file1: str, file2: str):
    with open(file1, "r", encoding="utf-8") as f:
        lines1 = f.readlines()
    with open(file2, "r", encoding="utf-8") as f:
        lines2 = f.readlines()

    diff = difflib.unified_diff(lines1, lines2, fromfile=file1, tofile=file2, lineterm="")
    result = list(diff)
    if result:
        print("\n".join(result))
        print(f"\n差异: {len([l for l in result if l.startswith('+') or l.startswith('-')])} 行")
    else:
        print("两个文件完全相同")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="文本对比")
    parser.add_argument("file1", help="文件1")
    parser.add_argument("file2", help="文件2")
    args = parser.parse_args()
    text_diff(args.file1, args.file2)
