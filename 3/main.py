from pathlib import Path
import re
from typing import Any, Generator


def read_input(file_path: Path) -> list[str]:
    """
    Reads the lines in a file into a list of strings.
    """
    with open(file_path) as f:
        lines = f.read().splitlines()
        return lines


def regex_iterator(pattern: str, text: str) -> Generator[Any, None, None]:
    yield from re.findall(pattern, text)


def part1() -> None:
    program = read_input(Path("input.txt"))

    total = 0
    for line in program:
        total += sum(
            int(m1) * int(m2) for m1, m2 in regex_iterator(r"mul\((\d+),(\d+)\)", line)
        )

    print(total)


def part2() -> None:
    program = read_input(Path("input.txt"))

    total = 0
    paused = False
    for line in program:
        for m in regex_iterator(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line):
            if m[2]:
                paused = False
            elif m[3]:
                paused = True
            else:
                total += int(m[0]) * int(m[1]) * (not paused)

    print(total)


part1()
part2()
