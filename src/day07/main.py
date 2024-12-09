from pathlib import Path
from itertools import product


def test_part1():
    assert part1("sample.txt") == 3749


def test_part2():
    assert part2("sample.txt") == 11387


def part1(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    answer = 0

    for line in lines:
        expected_res, components = line.split(": ")
        expected_res = int(expected_res)

        components = components.split(" ")
        components = [int(component) for component in components]

        operator_combinations = list(product(["+", "*"], repeat=len(components) - 1))

        for operator_combination in operator_combinations:
            curr_res = components[0]
            for idx, operator in enumerate(operator_combination):
                if operator == "+":
                    curr_res += components[idx + 1]
                else:
                    curr_res *= components[idx + 1]

                # current result is already greater than answer so we don't need to check
                if curr_res > expected_res:
                    break

            if curr_res == expected_res:
                answer += expected_res
                break

    return answer


def part2(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    answer = 0

    for line in lines:
        expected_res, components = line.split(": ")
        expected_res = int(expected_res)

        components = components.split(" ")
        components = [int(component) for component in components]

        operator_combinations = list(
            product(["+", "*", "||"], repeat=len(components) - 1)
        )

        for operator_combination in operator_combinations:
            curr_res = components[0]
            for idx, operator in enumerate(operator_combination):
                if operator == "+":
                    curr_res += components[idx + 1]
                elif operator == "*":
                    curr_res *= components[idx + 1]
                elif operator == "||":
                    curr_res = int(str(curr_res) + str(components[idx + 1]))

                # current result is already greater than answer so we don't need to check
                if curr_res > expected_res:
                    break

            if curr_res == expected_res:
                answer += expected_res
                break

    return answer


if __name__ == "__main__":
    print("\n------ day07 ------")
    test_part1()
    print("part1 answer: " + str(part1("input.txt")))

    test_part2()
    print("part2 answer: " + str(part2("input.txt")))
