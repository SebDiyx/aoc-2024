from pathlib import Path


def test_part1():
    assert part1("sample.txt") == 1928


def test_part2():
    assert part2("sample.txt") == 2858


def part1(filename: str):
    input = open(Path(__file__).parent / filename, "r").read()

    # Parse input into disk image
    file_id = 0
    disk: list[int | None] = []
    for idx, char in enumerate(input):
        is_file = idx % 2 == 0

        for _ in range(int(char)):
            if is_file:
                disk.append(file_id)
            else:
                disk.append(None)

        if is_file:
            file_id += 1

    # Group files into 1 block
    for idx in range(len(disk) - 1, 0, -1):
        file_id = disk[idx]

        if file_id is None:
            continue

        first_empty_idx = disk.index(None)

        if first_empty_idx > idx:
            break

        disk[first_empty_idx] = file_id
        disk[idx] = None

    # Check sum
    checksum = 0
    for idx, val in enumerate(disk):
        if val is None:
            break
        checksum += idx * val

    return checksum


def print_disk(disk: list[int | None]):
    for idx, val in enumerate(disk):
        if val is None:
            print(".", end="")
        else:
            print(val, end="")
    print()


def get_first_possible_slot(disk: list[int | None], file_length: int):
    empty_start = None
    empty_length = 0
    for idx, val in enumerate(disk):
        if val is None:
            empty_length += 1
            if empty_start is None:
                empty_start = idx

            if empty_length == file_length:
                return empty_start

        else:
            empty_start = None
            empty_length = 0

    return None


def part2(filename: str):
    input = open(Path(__file__).parent / filename, "r").read()

    # Parse input into disk image
    curr_file_id = 0
    disk: list[int | None] = []
    for idx, char in enumerate(input):
        is_file = idx % 2 == 0

        for _ in range(int(char)):
            if is_file:
                disk.append(curr_file_id)
            else:
                disk.append(None)

        if is_file:
            curr_file_id += 1

    # Defragment disk
    for id in range(curr_file_id - 1, 0, -1):
        print(f"curr file id: {id}")
        start_idx = disk.index(id)
        end_idx = len(disk) - disk[::-1].index(id) - 1
        length = end_idx - start_idx + 1

        # Find first empty slot that will fit the file
        empty_idx = get_first_possible_slot(disk, length)

        if empty_idx is None or empty_idx > start_idx:
            continue

        for idx in range(start_idx, end_idx + 1):
            disk[empty_idx] = disk[idx]
            disk[idx] = None
            empty_idx += 1

    # Check sum
    checksum = 0
    for idx, val in enumerate(disk):
        if val is None:
            continue
        checksum += idx * val

    return checksum


if __name__ == "__main__":
    print("\n------ day09 ------")
    # test_part1()
    # print("part1 answer: " + str(part1("input.txt")))

    test_part2()
    print("part2 answer: " + str(part2("input.txt")))
