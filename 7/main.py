from itertools import product
from pathlib import Path
from typing import Callable, Iterable


def read_input(file_path: Path) -> list[tuple[int, tuple[int, ...]]]:
    """
    Reads the lines in a file into a lists of character lists.
    """
    equations: list[tuple[int, tuple[int, ...]]] = []
    with open(file_path) as f:
        lines = f.read().splitlines()
        for l in lines:
            target, rest = l.split(":")
            equations.append((int(target), tuple(int(r) for r in rest.split())))

    return equations


def is_possible_to_obtain_target(
    target: int, nums: tuple[int, ...], operators: Iterable[Callable[[int, int], int]]
) -> bool:
    """
    Determines whether it is possible to reach the target number by applying any combination
    of operators left-to-right to the input numbers.
    """

    for operator_set in product(operators, repeat=len(nums) - 1):
        total = nums[0]
        for i, o in enumerate(operator_set, 1):
            total = o(total, nums[i])
        if total == target:
            return True
    return False


def p1() -> None:
    operators = [
        lambda total, number: total + number,
        lambda total, number: total * number
    ]

    total = 0
    for target, nums in read_input(Path("input.txt")):
        if is_possible_to_obtain_target(target, nums, operators):
            total += target

    print(total)


def p2() -> None:
    operators = [
        lambda total, number: total + number,
        lambda total, number: total * number,
        lambda total, number: int(str(total) + str(number)),
    ]

    total = 0
    for target, nums in read_input(Path("input.txt")):
        if is_possible_to_obtain_target(target, nums, operators):
            total += target

    print(total)


p1()
p2()
