from pathlib import Path
from math import ceil


def test_part1():
    assert part1("sample.txt") == 143


def test_part2():
    assert part2("sample.txt") == 123


def build_rules_map(rules_section: str):
    # Create a map of the before and after rules
    rules = rules_section.split("\n")
    rules_map = {}
    for rule in rules:
        [a, b] = rule.split("|")
        if a not in rules_map.keys():
            rules_map[a] = {
                "come_after": [],
                "come_before": [],
            }

        rules_map[a]["come_after"].append(b)

        if b not in rules_map.keys():
            rules_map[b] = {
                "come_after": [],
                "come_before": [],
            }

        rules_map[b]["come_before"].append(a)

    return rules_map


def is_valid(pages: list[str], rules_map: dict[str, dict[str, list[str]]]):
    valid = True
    swaps = []

    for i in range(len(pages)):
        page = pages[i]
        before_list = pages[slice(0, i)]
        after_list = pages[slice(i + 1, len(pages))]

        rules = rules_map.get(page)

        if rules is None:
            continue  # No rules for this page so its fine

        for before in before_list:
            if before in rules["come_after"]:
                swaps.append((before, page))
                valid = False

        for after in after_list:
            if after in rules["come_before"]:
                swaps.append((page, after))
                valid = False

        if not valid:
            break

    return valid, swaps


def part1(filename: str):
    with open(Path(f"src/day05/{filename}")) as file:
        input = file.read()

    rules_section, updates_section = input.split("\n\n")
    rules_map = build_rules_map(rules_section)

    answer = 0

    # Create a list of updates
    for line in updates_section.split("\n"):
        pages = line.split(",")

        valid, _ = is_valid(pages, rules_map)

        if valid:
            middle_idx = ceil(len(pages) / 2) - 1
            answer += int(pages[middle_idx])

    return answer


def part2(filename: str):
    with open(Path(f"src/day05/{filename}")) as file:
        input = file.read()

    rules_section, updates_section = input.split("\n\n")
    rules_map = build_rules_map(rules_section)

    answer = 0

    # Create a list of updates
    for line in updates_section.split("\n"):
        pages = line.split(",")

        valid, swaps = is_valid(pages, rules_map)

        if not valid:
            # Keep swapping until we have a valid list
            while not valid:
                for swap in swaps:
                    a, b = swap
                    a_idx = pages.index(a)
                    b_idx = pages.index(b)
                    pages[a_idx], pages[b_idx] = pages[b_idx], pages[a_idx]

                valid, swaps = is_valid(pages, rules_map)

            middle_idx = ceil(len(pages) / 2) - 1
            answer += int(pages[middle_idx])

    return answer


if __name__ == "__main__":
    print("\n------ day05 ------")
    test_part1()
    print("part1 answer: " + str(part1("input.txt")))

    test_part2()
    print("part2 answer: " + str(part2("input.txt")))
