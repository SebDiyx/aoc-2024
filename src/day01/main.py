from pathlib import Path

def test_part1():
    assert part1('sample.txt') == 11

def test_part2():
    assert part2('sample.txt') == 31

def part1(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    left_list: list[int] = []
    right_list: list[int] = []
    for line in lines:
        [left, right] = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))


    left_list.sort()
    right_list.sort()

    total = 0
    for idx, left in enumerate(left_list):
        right = right_list[idx]
        diff = abs(right - left)
        total += diff
       
    return total 

def part2(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    left_list: list[int] = []
    right_list: list[int] = []
    for line in lines:
        [left, right] = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    total = 0
    for left in left_list:
        count = right_list.count(left)
        total += left * count

    return total


if __name__ == "__main__":
    test_part1()
    print('part1 answer: ' + str(part1('input.txt')))

    test_part2()
    print('part2 answer: ' + str(part2('input.txt')))