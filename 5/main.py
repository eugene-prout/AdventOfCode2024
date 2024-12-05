from collections import defaultdict
from pathlib import Path
from typing import Container, Mapping, Optional, Sequence


def read_input(file_path: Path) -> tuple[list[tuple[int, int]], list[tuple[int]]]:
    with open(file_path) as f:
        lines = f.read().splitlines()

        ordering_rules = []
        i = 0
        while lines[i] != "":
            l = lines[i]
            parsed = l.split("|")
            ordering_rules.append((int(parsed[0]), int(parsed[1])))
            i += 1

        ordering_inputs = []
        i += 1
        while i < len(lines):
            l = lines[i]
            parsed = l.split(",")
            ordering_inputs.append(tuple(int(p) for p in parsed))
            i += 1

        return ordering_rules, ordering_inputs


def group_tuples_into_dict(l: list[tuple[int, int]]) -> dict[int, list[int]]:
    d = defaultdict(list)
    for u, v in l:
        d[u].append(v)

    return d


def index_invalidating_ordering(ordering: Sequence[int], rules: Mapping[int, Container[int]]) -> Optional[int]:
    for i in range(len(ordering)):
        if any(z in rules[ordering[i]] for z in ordering[:i]):
            return i
    return None


def get_middle_element(l: list):
    return l[len(l) // 2]


def p1() -> None:
    rules, orderings = read_input(Path("input.txt"))
    rules_dict = group_tuples_into_dict(rules)
    total = sum(get_middle_element(l) for l in orderings if not index_invalidating_ordering(l, rules_dict))  # type: ignore
    print(total)


def p2() -> None:
    rules, orderings = read_input(Path("input.txt"))
    rules_dict = group_tuples_into_dict(rules)

    incorrect_orders = [list(l) for l in orderings if index_invalidating_ordering(l, rules_dict)]
    for z in incorrect_orders:
        while incorrect_index := index_invalidating_ordering(z, rules_dict):
            z[incorrect_index], z[incorrect_index - 1] = z[incorrect_index - 1], z[incorrect_index]

    total = sum(map(get_middle_element, incorrect_orders))
    print(total)
