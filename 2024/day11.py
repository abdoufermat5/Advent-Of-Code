def read_file(file_path):
    with open(file_path) as f:
        return list(map(int, f.readlines()[0].split(" ")))


def is_even(stone_number: int):
    return len(str(stone_number)) % 2 == 0


def split_even_stone(stone_number):
    str_stone = str(stone_number)
    n = len(str_stone)
    return [int(str_stone[:n // 2]), int(str_stone[n // 2:])]


def blink(stone_list: list) -> list:
    res = []
    for el in stone_list:
        if el == 0:
            res.append(1)
        elif is_even(el):
            res.extend(split_even_stone(el))
        else:
            res.append(el * 2024)
    return res


def plutonian_pebbles(stone_list, n=25):
    stone_counts = {stone: 1 for stone in stone_list}

    for _ in range(n):
        new_counts = {}
        for stone, count in stone_counts.items():
            transformed = blink([stone])
            for new_stone in transformed:
                new_counts[new_stone] = new_counts.get(new_stone, 0) + count
        stone_counts = new_counts

    return sum(stone_counts.values())


if __name__ == "__main__":
    realInput = "../data/2024/day11Input.txt"
    testInput = "./test.txt"

    data = read_file(realInput)

    print(plutonian_pebbles(data))
    print(plutonian_pebbles(data, 75))

# first output: 4569
# second output: 6456
