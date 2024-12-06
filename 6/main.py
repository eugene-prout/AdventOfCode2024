from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Optional


class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    @staticmethod
    def from_ascii(c: str):
        match c:
            case "^":
                return Direction.N
            case ">":
                return Direction.E
            case "<":
                return Direction.W
            case "v":
                return Direction.S
            case _:
                raise ValueError(f"No enum value for {c}.")

    @staticmethod
    def rotate_90_right(d: Any):
        match d:
            case Direction.N:
                return Direction.E
            case Direction.E:
                return Direction.S
            case Direction.W:
                return Direction.N
            case Direction.S:
                return Direction.W
            case _:
                raise ValueError(f"No rotate value for {d}.")


@dataclass(frozen=True)
class Position:
    pos: tuple[int, int]
    direction: Direction


def parse_input(file_path: Path) -> tuple[dict[tuple[int, int], bool], Position]:
    obstacle_map: dict[tuple[int, int], bool] = {}
    starting_position: Optional[Position] = None

    with open(file_path) as f:
        lines = f.read().splitlines()
        for i, l in enumerate(lines):
            for j, s in enumerate(l):
                if s == ".":
                    obstacle_map[(i, j)] = False
                elif s == "#":
                    obstacle_map[(i, j)] = True
                elif s in ("^", ">", "v", "<"):
                    obstacle_map[(i, j)] = False
                    starting_position = Position((i, j), Direction.from_ascii(s))
                else:
                    raise ValueError(f"Unsupported symbol {s}.")

    if starting_position == None:
        raise ValueError("Grid contains no start position.")

    return obstacle_map, starting_position


def step_through_grid(grid: dict[tuple[int, int], bool], position: Position) -> Optional[Position]:
    """
    From a given position in a given grid, compute 1 movement step.
    Returns the updated position if in bounds, otherwise None.
    """
    match position.direction:
        case Direction.N:
            new_pos = (position.pos[0] - 1, position.pos[1])
        case Direction.E:
            new_pos = (position.pos[0], position.pos[1] + 1)
        case Direction.W:
            new_pos = (position.pos[0], position.pos[1] - 1)
        case Direction.S:
            new_pos = (position.pos[0] + 1, position.pos[1])

    if new_pos not in grid:
        return None

    if grid[new_pos]:
        return Position(position.pos, Direction.rotate_90_right(position.direction))
    else:
        return Position(new_pos, position.direction)


def has_cycle(grid: dict[tuple[int, int], bool], pos: Position) -> bool:
    """
    Determines whether moving from the given position in the given grid causes a cycle of repeating position.
    """
    position_set: set[Position] = {pos}
    while pos := step_through_grid(grid, pos):  # type: ignore
        if pos in position_set:
            return True
        else:
            position_set.add(pos)

    return False


def p1() -> None:
    grid, pos = parse_input(Path("input.txt"))

    position_set: set[tuple[int, int]] = {pos.pos}
    while pos := step_through_grid(grid, pos):
        position_set.add(pos.pos)

    print(len(position_set))


def p2() -> None:
    grid, pos = parse_input(Path("input.txt"))

    cycle_making_count = 0
    for coordinate, value in grid.items():
        # No need to check for a cycle if the cell already contains an obstacle.
        if value == True:
            continue
        else:
            grid[coordinate] = True
            if has_cycle(grid, pos):
                cycle_making_count += 1
            grid[coordinate] = False

    print(cycle_making_count)
