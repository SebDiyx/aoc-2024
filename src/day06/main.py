from pathlib import Path

class Gaurd:
    direction: str
    x: int
    y: int
    history: list[(str, int, int)]

    def __init__(self, grid):
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if char == "^":
                    self.x = x
                    self.y = y

        self.direction = "north"
        self.history= []
    
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
                return True
            return grid[self.y-1][self.x] == "#"
        elif self.direction == "east":
            if self.x == len(grid[0]) - 1:
                return True
            return grid[self.y][self.x+1] == "#"
        elif self.direction == "south":
            if self.y == len(grid) - 1:
                return True
            return grid[self.y+1][self.x] == "#"
        elif self.direction == "west":
            if self.x == 0: 
                return True
            return grid[self.y][self.x-1] == "#"

    def has_looped(self):
        return (self.direction, self.x, self.y) in self.history
    
    def tick(self, grid):
        if self.is_facing_object(grid):
            self.turn_right()
        else:
            self.move_forward()


def test_part1():
    assert part1('sample.txt') == 41

def test_part2():
    assert part2('sample.txt') == -1

def part1(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    grid = file.strip().split("\n")
   

    gaurd = Gaurd(grid)

    while not gaurd.has_looped():
        gaurd.tick(grid)

    print(len(gaurd.history))
    return len(gaurd.history)


    
def part2(filename: str):       
    print("TODO")


if __name__ == "__main__":
    test_part1()
    print('part1 answer: ' + str(part1('input.txt')))

    # test_part2()
    # print('part2 answer: ' + str(part2('input.txt')))