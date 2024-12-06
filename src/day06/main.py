from pathlib import Path


class Guard:
    direction: str
    x: int
    y: int
    unique_locations: set[(int, int)]
    history: list[(str, int, int)]

    def __init__(self, grid):
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if char == "^":
                    self.x = x
                    self.y = y

        self.direction = "north"
        self.unique_locations = set()
        self.history = []

    def turn_right(self):
        if self.direction == "north":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "south"
        elif self.direction == "south":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "north"

    def move_forward(self):
        self.unique_locations.add((self.x, self.y))
        self.history.append((self.direction, self.x, self.y))

        if self.direction == "north":
            self.y -= 1
        elif self.direction == "east":
            self.x += 1
        elif self.direction == "south":
            self.y += 1
        elif self.direction == "west":
            self.x -= 1

    def is_facing_object(self, grid):
        if self.direction == "north":
            if self.y == 0:
                return False
            return grid[self.y - 1][self.x] == "#"
        elif self.direction == "east":
            if self.x == len(grid[0]) - 1:
                return False
            return grid[self.y][self.x + 1] == "#"
        elif self.direction == "south":
            if self.y == len(grid) - 1:
                return False
            return grid[self.y + 1][self.x] == "#"
        elif self.direction == "west":
            if self.x == 0:
                return False
            return grid[self.y][self.x - 1] == "#"

    def is_outside(self, grid):
        return self.x < 0 or self.x >= len(grid[0]) or self.y < 0 or self.y >= len(grid)

    def has_looped(self):
        return (self.direction, self.x, self.y) in self.history

    def tick(self, grid):
        if self.is_facing_object(grid):
            self.turn_right()
        else:
            self.move_forward()

    def print_grid(self, grid):
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if (x, y) in self.unique_locations:
                    print("X", end="")
                else:
                    print(char, end="")
            print()
        print()


def test_part1():
    assert part1("sample.txt") == 41


def test_part2():
    assert part2("sample.txt") == 6


def part1(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    grid = file.strip().split("\n")

    guard = Guard(grid)

    while not guard.is_outside(grid):
        guard.tick(grid)

    return len(guard.unique_locations)


def part2(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")
    grid = [list(line) for line in lines]

    base_guard = Guard(grid)
    while not base_guard.is_outside(grid):
        base_guard.tick(grid)

    idx = 0
    answer = 0
    for loc in base_guard.unique_locations:
        idx += 1
        print(str(idx / len(base_guard.unique_locations) * 100) + "%")

        x, y = loc

        if grid[y][x] != ".":
            continue

        grid[y][x] = "#"
        guard = Guard(grid)
        while not guard.is_outside(grid) and not guard.has_looped():
            guard.tick(grid)
            if guard.has_looped():
                answer += 1

        grid[y][x] = "."

    return answer


if __name__ == "__main__":
    print("\n------ day06 ------")
    test_part1()
    print("part1 answer: " + str(part1("input.txt")))

    test_part2()
    print("part2 answer: " + str(part2("input.txt")))
