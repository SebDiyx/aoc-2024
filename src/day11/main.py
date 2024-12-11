from functools import cache
from pathlib import Path


def test_part1():
    assert part1("sample.txt") == 55312


def test_part2():
    assert part2("sample.txt", 25) == 55312


def part1(filename: str):
    input = open(Path(__file__).parent / filename, "r").read()
    stones = input.split(" ")

    BLINKS = 25
    for _ in range(BLINKS):
        new_stones = []
        for stone in stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone) % 2 == 0:
                # Split in half
                first_half = stone[:len(stone)//2]
                second_half = stone[len(stone)//2:]
                new_stones.append(first_half)
                new_stones.append(str(int(second_half)))  # Handles multiple 0s
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones

    return (len(stones))


@cache
def blink(stone: str, blinks: int):
    # Done blinking
    if blinks == 0:
        return 1

    if stone == "0":
        return blink("1", blinks-1)
    elif len(stone) % 2 == 0:
        # Split in half
        first_half = stone[:len(stone)//2]
        second_half = stone[len(stone)//2:]
        return blink(first_half, blinks-1) + blink(str(int(second_half)), blinks-1)
    else:
        return blink(str(int(stone) * 2024), blinks-1)


def part2(filename: str, blinks: int):
    input = open(Path(__file__).parent / filename, "r").read()
    stones = input.split(" ")

    answer = 0
    for stone in stones:
        answer += blink(stone, blinks)

    return answer


if __name__ == "__main__":
    # print("\n------ day11 ------")
    # test_part1()
    # print("part1 answer: " + str(part1("input.txt")))

    test_part2()
    print("part2 answer: " + str(part2("input.txt", 75)))
