#!/usr/bin/env python3
"""JSON 格式化工具"""

import json
import argparse


def format_json(input_file: str, output_file: str = None, indent: int = 2):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    output = output_file or input_file
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
    print(f"格式化完成: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JSON 格式化")
    parser.add_argument("input", help="输入文件")
    parser.add_argument("--output", help="输出文件")
    parser.add_argument("--indent", type=int, default=2, help="缩进空格数")
    args = parser.parse_args()
    format_json(args.input, args.output, args.indent)
