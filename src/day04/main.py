from pathlib import Path


def test_part1():
    assert part1("sample.txt") == 18


def test_part2():
    assert part2("sample.txt") == 9


def update_tracker(
    tracker: list[list[str]], x: int, y: int, direction_parts: list[dict]
):
    xmas = "XMAS"
    tracker[y][x] = xmas[0]
    for i, direction_part in enumerate(direction_parts):
        tracker[y + direction_part["y"]][x + direction_part["x"]] = xmas[i + 1]


def print_tracker(tracker: list[str]):
    print("\n")
    for line in tracker:
        for char in line:
            print(char, end="")
        print()
    print("\n")


def is_outside(x: int, y: int, width: int, height: int):
    return x < 0 or x >= width or y < 0 or y >= height


def part1(filename: str):
    with open(Path(f"src/day04/{filename}")) as file:
        lines = file.read().split("\n")

    width = len(lines[0])
    height = len(lines)

    directions = [
        [{"x": 0, "y": -1}, {"x": 0, "y": -2}, {"x": 0, "y": -3}],
        [{"x": 1, "y": -1}, {"x": 2, "y": -2}, {"x": 3, "y": -3}],
        [{"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}],
        [{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": 3}],
        [{"x": 0, "y": 1}, {"x": 0, "y": 2}, {"x": 0, "y": 3}],
        [{"x": -1, "y": 1}, {"x": -2, "y": 2}, {"x": -3, "y": 3}],
        [{"x": -1, "y": 0}, {"x": -2, "y": 0}, {"x": -3, "y": 0}],
        [{"x": -1, "y": -1}, {"x": -2, "y": -2}, {"x": -3, "y": -3}],
    ]

    tracker = []
    for i in range(height):
        tracker.append(["."] * width)

    answer = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            # We're only searching for XMAS so we can skip the rest
            if char != "X":
                continue

            # If we've found an X, we need to check all directions for XMAS
            for direction in directions:
                combination = "X"
                for offset in direction:
                    y_offset = y + offset["y"]
                    x_offset = x + offset["x"]
                    if is_outside(x_offset, y_offset, width, height):
                        break
                    combination += lines[y_offset][x_offset]

                if combination == "XMAS":
                    update_tracker(tracker, x, y, direction)
                    answer += 1

    return answer


def part2(filename: str):
    with open(Path(f"src/day04/{filename}")) as file:
        lines = file.read().split("\n")

    width = len(lines[0])
    height = len(lines)

    answer = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            # We're only searching for A in the center
            if char != "A":
                continue

            if (
                is_outside(x - 1, y - 1, width, height)
                or is_outside(x + 1, y + 1, width, height)
                or is_outside(x - 1, y + 1, width, height)
                or is_outside(x + 1, y - 1, width, height)
            ):
                continue

            # if we've found an A, we need to check each corner for M & S
            opposite_corners = [
                [lines[y - 1][x - 1], lines[y + 1][x + 1]],
                [lines[y + 1][x - 1], lines[y - 1][x + 1]],
            ]
            if (
                "M" in opposite_corners[0]
                and "S" in opposite_corners[0]
                and "M" in opposite_corners[1]
                and "S" in opposite_corners[1]
            ):
                answer += 1

    return answer


if __name__ == "__main__":
    print("------ day04 ------")
    test_part1()
    print("part1 answer: " + str(part1("input.txt")))

    test_part2()
    print("part2 answer: " + str(part2("input.txt")))
