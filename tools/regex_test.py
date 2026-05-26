#!/usr/bin/env python3
"""正则表达式测试工具"""

import re
import argparse


def test_regex(pattern: str, text: str, flags: str = ""):
    f = 0
    if "i" in flags:
        f |= re.IGNORECASE
    if "m" in flags:
        f |= re.MULTILINE
    if "s" in flags:
        f |= re.DOTALL

    matches = re.findall(pattern, text, f)
    print(f"模式: {pattern}")
    print(f"匹配数: {len(matches)}")
    for i, m in enumerate(matches[:20], 1):
        print(f"  [{i}] {m}")
    if len(matches) > 20:
        print(f"  ... 还有 {len(matches) - 20} 个匹配")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="正则表达式测试")
    parser.add_argument("--pattern", required=True, help="正则表达式")
    parser.add_argument("--text", required=True, help="测试文本")
    parser.add_argument("--flags", default="", help="标志: i(ignorecase) m(multiline) s(dotall)")
    args = parser.parse_args()
    test_regex(args.pattern, args.text, args.flags)
