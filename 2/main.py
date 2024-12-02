from pathlib import Path
from typing import Any, Generator


def stream_input(file_path: Path) -> Generator[tuple[int, ...], Any, Any]:
    """
    Reads a file containing 2 columns and an answer into a structured format.

    For example:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9

    is returned as

    [(7, 6, 4, 2, 1), (1, 2, 7, 8, 9), (9, 7, 6, 2, 1), (1, 3, 2, 4, 5), (8, 6, 4, 4, 1), (1, 3, 6, 7, 9)]
    """
    with open(file_path) as f:
        lines = f.read().splitlines()
        for l in lines:
            if l == "":
                break
            parsed_line = tuple(map(int, l.split(" ")))
            yield parsed_line


def is_report_safe(l: tuple[int, ...]):
    increasing = l[0] < l[1]
    for prev, next in zip(l, l[1:]):
        if abs(next - prev) < 1 or abs(next - prev) > 3:
            return False
        elif increasing and next <= prev:
            return False
        elif not increasing and next >= prev:
            return False
    return True


def get_one_element_removed[T](l: list[T]) -> Generator[tuple[T, ...], Any, Any]:
    """
    Returns all possible lists after removing 1 element from the input list.
    """
    for i in range(len(l)):
        temp = l.copy()
        temp.pop(i)
        yield tuple(temp)


def part_1():
    reports = stream_input(Path("p1.txt"))
    return sum(is_report_safe(report) for report in reports)


def part_2() -> int:
    reports = stream_input(Path("p1.txt"))
    is_report_safe_with_one_removed = lambda r: any(
        is_report_safe(one_removed) for one_removed in get_one_element_removed(list(r))
    )
    return sum(map(is_report_safe_with_one_removed, reports))
