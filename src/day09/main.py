from pathlib import Path


def test_part1():
    assert part1("sample.txt") == 1928


def test_part2():
    assert part2("sample.txt") == 6


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
    for idx in range(len(disk)-1, 0, -1):
        file_id = disk[idx]

        if file_id is None:
            continue

        first_empty_idx = disk.index(None)

        if (first_empty_idx > idx):
            break

        disk[first_empty_idx] = file_id
        disk[idx] = None

    # Check sum
    checksum = 0
    for idx, val in enumerate(disk):
        if (val is None):
            break
        checksum += idx * val

    return checksum


def part2(filename: str):
    input = open(Path(__file__).parent / filename, "r").read()

    # Parse input into disk image
    file_id = 0
    curr_start = 0
    disk = []
    for idx, char in enumerate(input):
        is_file = idx % 2 == 0
        length = int(char)

        if is_file:
            disk.append({
                "type": "file",
                "id": file_id,
                "start": curr_start,
                "end": curr_start + length - 1
            })
        else:
            disk.append({
                "type": "empty",
                "start": curr_start,
                "end": curr_start + length - 1
            })

        curr_start += length

        if is_file:
            file_id += 1

    # Fragment files
    for curr_file_id in range(file_id-1, 0, -1):
        file_details = filter(lambda x: x["type"]
                              == "file" and x["id"] == curr_file_id, disk)

        file_length = file_details["end"] - file_details["start"] + 1
        first_empty_idx = disk.find(
            lambda x: x["type"] == "empty" and x["end"] - x["start"] + 1 >= file_length)

        if (first_empty_idx > file_details["start"]):
            break

        # Swap the file with the empty block
        disk[first_empty_idx] = {
            "type": "file",
            "id": curr_file_id,
            "start": disk[first_empty_idx]["start"],
            "end": disk[first_empty_idx]["start"] + file_length - 1
        }

        disk[] = {
            "type": "empty",
            "start": file_details["start"],
            "end": file_details["end"]
        }

    # Check sum
    checksum = 0
    for idx, val in enumerate(disk):
        if (val is None):
            break
        checksum += idx * val

    return checksum


if __name__ == "__main__":
    print("\n------ day09 ------")
    test_part1()
    print("part1 answer: " + str(part1("input.txt")))

    # test_part2()
    # print("part2 answer: " + str(part2("input.txt")))
