from collections import Counter
from pathlib import Path
from typing import Any, Generator


def stream_input(file_path: Path) -> Generator[tuple[int, int], Any, Any]:
    """
    Reads a file containing 2 columns and an answer into a structured format.

    For example:

    3   4
    4   3
    2   5
    1   3
    3   9
    3   3

    is returned as

    [(3, 4), (4, 3), (2, 5), (1, 3), (3, 9), (3, 3)]
    """
    with open(file_path) as f:
        lines = f.read().splitlines()
        for l in lines:
            if l == "":
                break
            parsed_line = tuple(map(int, l.split("   ")))
            if len(parsed_line) != 2:
                raise ValueError(f"Invalid line format: {l}")
            yield parsed_line


def part1():
    input_lines = list(stream_input(Path("p1.txt")))
    left_list, right_list = map(sorted, list(zip(*input_lines)))

    print(sum(abs(left_list[i] - right_list[i]) for i in range(len(left_list))))


def part2():
    input_lines = list(stream_input(Path("p1.txt")))
    left_list, right_list = map(sorted, list(zip(*input_lines)))

    right_list_counts = Counter(right_list)

    print(sum(i * right_list_counts.get(i, 0) for i in left_list))
