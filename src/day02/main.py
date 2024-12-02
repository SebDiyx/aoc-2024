from pathlib import Path

def test_part1():
    assert part1('sample.txt') == 2

def test_part2():
    assert part2('sample.txt') == 4

def part1(filename: str):
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    answer = 0
    for line in lines:
        report_levels = list(map(int, line.split(" ")))

        is_valid_report = True

        is_increasing = (report_levels[1] - report_levels[0]) > 0
        prev_level = report_levels.pop(0)

        while(is_valid_report and len(report_levels) > 0):
            level = report_levels.pop(0)

            diff = level - prev_level
            if(not is_increasing):
                diff = diff * -1

            valid_diff = diff >= 1 and diff <= 3
            if(not valid_diff):
                is_valid_report = False

            prev_level = level

        if(is_valid_report):
            answer += 1

    return answer

    
def part2(filename: str):       
    file = open(Path(__file__).parent / filename, "r").read()
    lines = file.strip().split("\n")

    answer = 0
    for line in lines:
        report_levels = list(map(int, line.split(" ")))

        for idx_to_ignore, ignored_level in enumerate(report_levels):
            reduced_report_levels = report_levels.copy()
            reduced_report_levels.pop(idx_to_ignore)

            is_valid_report = True

            is_increasing = (reduced_report_levels[1] - reduced_report_levels[0]) > 0

            for idx, level in enumerate(reduced_report_levels):
                if(idx == 0): 
                    continue

                prev_level = reduced_report_levels[idx-1]

                diff = level - prev_level
                if(not is_increasing):
                    diff = diff * -1

                valid_diff = diff >= 1 and diff <= 3
                if(not valid_diff):
                    is_valid_report = False

            if(is_valid_report):
                answer += 1
                break

    return answer

if __name__ == "__main__":
    test_part1()
    print('part1 answer: ' + str(part1('input.txt')))

    test_part2()
    print('part2 answer: ' + str(part2('input.txt')))