#!/usr/bin/env python3
"""快捷命令集"""

import os
import subprocess
import argparse


def disk_usage(path: str = "."):
    """查看磁盘使用情况"""
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                total += os.path.getsize(fp)
            except OSError:
                pass
    print(f"目录 {path} 总大小: {total / 1024 / 1024:.2f} MB")


def find_large_files(path: str = ".", size_mb: float = 10):
    """查找大文件"""
    threshold = size_mb * 1024 * 1024
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                s = os.path.getsize(fp)
                if s > threshold:
                    print(f"  {s / 1024 / 1024:.1f}MB  {fp}")
            except OSError:
                pass


def count_lines(path: str = ".", ext: str = ".py"):
    """统计代码行数"""
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(ext):
                fp = os.path.join(root, f)
                try:
                    with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                        total += sum(1 for _ in fh)
                except OSError:
                    pass
    print(f"{ext} 文件总行数: {total}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="快捷命令集")
    sub = parser.add_subparsers(dest="command")

    du = sub.add_parser("du", help="查看目录大小")
    du.add_argument("--path", default=".")

    large = sub.add_parser("large", help="查找大文件")
    large.add_argument("--path", default=".")
    large.add_argument("--size", type=float, default=10)

    lines = sub.add_parser("lines", help="统计代码行数")
    lines.add_argument("--path", default=".")
    lines.add_argument("--ext", default=".py")

    args = parser.parse_args()
    if args.command == "du":
        disk_usage(args.path)
    elif args.command == "large":
        find_large_files(args.path, args.size)
    elif args.command == "lines":
        count_lines(args.path, args.ext)
    else:
        parser.print_help()
