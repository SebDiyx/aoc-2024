from pathlib import Path
import re

def test_part1():
    assert part1('sample1.txt') == 161

def test_part2():
    assert part2('sample2.txt') == 48

def part1(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    pattern = r'mul\(\d+,\d+\)'
    answer = 0
    for line in lines:

        formulas = re.findall(pattern, line)
        for formula in formulas:
            nums = formula.replace("mul(", "").replace(")", "").split(",")
            answer += int(nums[0]) * int(nums[1])
        
    return answer

    
def part2(filename: str):       
    file = open(Path(__file__).parent / filename, "r").read()
    input = file.strip().replace("\n", "")

    answer = 0
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    parts = re.findall(pattern, input)
    can_add = True
    for part in parts:
        if part == "do()":
            can_add = True
        elif part == "don't()":
            can_add = False
        elif can_add:
            nums = part.replace("mul(", "").replace(")", "").split(",")
            answer += int(nums[0]) * int(nums[1])
        
    return answer

if __name__ == "__main__":
    test_part1()
    print('part1 answer: ' + str(part1('input.txt')))

    test_part2()
    print('part2 answer: ' + str(part2('input.txt')))