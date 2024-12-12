from functools import cache
from pathlib import Path


def test_part1():
    assert part1("sample.txt") == 36


def test_part2():
    assert part2("sample.txt") == 55312


# -----------------------------------------------------------------------------


def is_out_of_bounds(lines: list[str], x: int, y: int):
    width = len(lines[0])
    height = len(lines)
    return x > width - 1 or x < 0 or y > height - 1 or y < 0


def check_point(
    lines: list[str], x: int, y: int, ends: set[(int, int)], history: list[(int, int)]
):
    height = int(lines[y][x])
    history.append((x, y))

    # up, right, down, left
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for dx, dy in movements:
        new_x = x + dx
        new_y = y + dy

        if is_out_of_bounds(lines, new_x, new_y):
            continue

        if (new_x, new_y) in history:
            continue

        new_height = int(lines[new_y][new_x])

        if new_height == 9:
            ends.add((new_x, new_y))
        elif new_height == height + 1:
            check_point(lines, new_x, new_y, ends, history)


def part1(filename: str):
    input = open(Path(__file__).parent / filename, "r").read()
    lines = input.split("\n")

    # Find all the locations of trailheads (0s in grid)
    trailheads = []
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            if height == "0":
                trailheads.append((x, y))

    # Get the score for each trailhead
    total = 0
    for x, y in trailheads:
        print(x, y)
        history = []
        ends = set()
        check_point(lines, x, y, ends, history)
        print(history)
        total += len(ends)

    return total


def part2(filename: str):
    input = open(Path(__file__).parent / filename, "r").read()


if __name__ == "__main__":
    print("\n------ day10 ------")
    test_part1()
    print("part1 answer: " + str(part1("input.txt")))

    # test_part2()
    # print("part2 answer: " + str(part2("input.txt")))
