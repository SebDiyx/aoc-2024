from pathlib import Path

def test_part1():
    assert part1('sample.txt') == -1

def test_part2():
    assert part2('sample.txt') == -1

def part1(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    answer = 0
    for line in lines:
        line.split(" ")
        
    return answer

    
def part2(filename: str):       
    print("TODO")


if __name__ == "__main__":
    test_part1()
    print('part1 answer: ' + str(part1('input.txt')))

    # test_part2()
    # print('part2 answer: ' + str(part2('input.txt')))