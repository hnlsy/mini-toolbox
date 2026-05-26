#!/usr/bin/env python3
"""批量文本替换工具"""

import os
import argparse


def batch_replace(folder: str, old: str, new: str, ext: str = ".txt"):
    """批量替换文件夹内文件的文本"""
    count = 0
    for root, _, files in os.walk(folder):
        for fname in files:
            if fname.endswith(ext):
                fpath = os.path.join(root, fname)
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                if old in content:
                    content = content.replace(old, new)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)
                    count += 1
                    print(f"  替换: {fname}")
    print(f"完成: 共替换 {count} 个文件")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="批量文本替换")
    parser.add_argument("--folder", default=".", help="目标文件夹")
    parser.add_argument("--old", required=True, help="要替换的文本")
    parser.add_argument("--new", default="", help="替换为")
    parser.add_argument("--ext", default=".txt", help="文件扩展名")
    args = parser.parse_args()
    batch_replace(args.folder, args.old, args.new, args.ext)
