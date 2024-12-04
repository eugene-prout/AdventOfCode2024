from pathlib import Path


def read_input(file_path: Path) -> list[list[str]]:
    """
    Reads the lines in a file into a lists of character lists.
    """
    with open(file_path) as f:
        lines = f.read().splitlines()
        return [list(l) for l in lines]


def in_dict_and_eq(k, d, e) -> bool:
    """
    Checks if a dictionary key has certain value. Returns false if the key is not in the dictionary.
    """
    return k in d and d[k] == e


def nd_array_into_map(array) -> dict:
    """
    Turns a 2d array into map of indices to values.
    """
    cells = {}
    for i in range(len(array)):
        for j in range(len(array[i])):
            cells[(i, j)] = array[i][j]
    return cells


def p1(grid: list[list[str]]) -> None:
    cells = nd_array_into_map(grid)

    total = 0
    for (x, y), character in cells.items():
        if character == "X":
            # N
            if (
                in_dict_and_eq((x - 1, y), cells, "M")
                and in_dict_and_eq((x - 2, y), cells, "A")
                and in_dict_and_eq((x - 3, y), cells, "S")
            ):
                total += 1
            # S
            if (
                in_dict_and_eq((x + 1, y), cells, "M")
                and in_dict_and_eq((x + 2, y), cells, "A")
                and in_dict_and_eq((x + 3, y), cells, "S")
            ):
                total += 1
            # E
            if (
                in_dict_and_eq((x, y + 1), cells, "M")
                and in_dict_and_eq((x, y + 2), cells, "A")
                and in_dict_and_eq((x, y + 3), cells, "S")
            ):
                total += 1
            # W
            if (
                in_dict_and_eq((x, y - 1), cells, "M")
                and in_dict_and_eq((x, y - 2), cells, "A")
                and in_dict_and_eq((x, y - 3), cells, "S")
            ):
                total += 1
            # NW
            if (
                in_dict_and_eq((x - 1, y - 1), cells, "M")
                and in_dict_and_eq((x - 2, y - 2), cells, "A")
                and in_dict_and_eq((x - 3, y - 3), cells, "S")
            ):
                total += 1
            # NE
            if (
                in_dict_and_eq((x - 1, y + 1), cells, "M")
                and in_dict_and_eq((x - 2, y + 2), cells, "A")
                and in_dict_and_eq((x - 3, y + 3), cells, "S")
            ):
                total += 1
            # SE
            if (
                in_dict_and_eq((x + 1, y + 1), cells, "M")
                and in_dict_and_eq((x + 2, y + 2), cells, "A")
                and in_dict_and_eq((x + 3, y + 3), cells, "S")
            ):
                total += 1
            # SW
            if (
                in_dict_and_eq((x + 1, y - 1), cells, "M")
                and in_dict_and_eq((x + 2, y - 2), cells, "A")
                and in_dict_and_eq((x + 3, y - 3), cells, "S")
            ):
                total += 1

    print(total)


def p2(grid: list[list[str]]) -> None:
    cells = nd_array_into_map(grid)

    total = 0
    for (x, y), character in cells.items():
        count = 0
        if character == "A":
            # Direction is the way M->S points.
            # NW
            if in_dict_and_eq((x + 1, y + 1), cells, "M") and in_dict_and_eq((x - 1, y - 1), cells, "S"):
                count += 1
            # NE
            if in_dict_and_eq((x + 1, y - 1), cells, "M") and in_dict_and_eq((x - 1, y + 1), cells, "S"):
                count += 1
            # SE
            if in_dict_and_eq((x - 1, y - 1), cells, "M") and in_dict_and_eq((x + 1, y + 1), cells, "S"):
                count += 1
            # SW
            if in_dict_and_eq((x - 1, y + 1), cells, "M") and in_dict_and_eq((x + 1, y - 1), cells, "S"):
                count += 1

            if count >= 2:
                total += 1

    print(total)
