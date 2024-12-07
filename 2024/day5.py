def read_file(file_path: str):
    with open(file_path, "r") as f:
        top, bottom = f.read().split("\n\n")
        top = top.split("\n")
        bottom = bottom.split("\n")
        return top, bottom


def handle_top(arr):
    d = {}
    for el in arr:
        a, b = el.split("|")
        if int(a) not in d:
            d[int(a)] = set()
        d[int(a)].add(int(b))

    return d


def is_valid_order(sequence, graph):
    # For each pair of numbers in the sequence
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            before = sequence[i]
            after = sequence[j]

            # Check if there's a rule saying after should come before before
            if after in graph and before in graph[after]:
                return False

    return True


def correct_line(sequence, graph):
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            before = sequence[i]
            after = sequence[j]

            # Check if there's a rule saying after should come before before
            if after in graph and before in graph[after]:
                sequence[i], sequence[j] = after, before
    return sequence


def print_queue(data, v2=False):
    correct_order_dict = handle_top(data[0])
    res = 0
    res2 = 0
    for line in data[1]:
        line = list(map(int, line.split(",")))
        is_correct = is_valid_order(line, correct_order_dict)
        if is_correct:
            res += line[len(line) // 2]
        if v2 and not is_correct:
            corrected = correct_line(line, correct_order_dict)
            res2 += corrected[len(corrected) // 2]
    return res2 if v2 else res


if __name__ == "__main__":
    testInput = "./test.txt"
    realInput = "../data/2024/day5Input.txt"
    data = read_file(realInput)
    print(print_queue(data))
    print(print_queue(data, v2=True))

# first output: 4569
# second output: 6456
