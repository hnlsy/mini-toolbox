#!/usr/bin/env python3
"""文件批量重命名工具"""

import os
import argparse
import glob


def batch_rename(folder: str, pattern: str, ext: str = None):
    files = glob.glob(os.path.join(folder, "*"))
    if ext:
        files = [f for f in files if f.endswith(ext)]
    files.sort()

    for i, fpath in enumerate(files, 1):
        directory = os.path.dirname(fpath)
        old_name = os.path.basename(fpath)
        file_ext = os.path.splitext(old_name)[1]
        new_name = pattern.replace("{n}", str(i).zfill(3)).replace("{ext}", file_ext)
        new_path = os.path.join(directory, new_name)
        os.rename(fpath, new_path)
        print(f"  {old_name} -> {new_name}")
    print(f"完成: 重命名 {len(files)} 个文件")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="文件批量重命名")
    parser.add_argument("--folder", required=True, help="目标文件夹")
    parser.add_argument("--pattern", required=True, help="命名模式 (用 {n} 代表序号, {ext} 代表扩展名)")
    parser.add_argument("--ext", help="只处理指定扩展名")
    args = parser.parse_args()
    batch_rename(args.folder, args.pattern, args.ext)
