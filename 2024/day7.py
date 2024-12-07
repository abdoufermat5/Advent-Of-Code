def read_file(file_path):
    with open(file_path, "r") as f:
        res = []
        for line in f.readlines():
            s, x = line.split(":")
            res.append((int(s), list(map(int, x.split()))))
    return res


def compute_operations(target, values, current_res=0, index=0, ops=[]):
    # Base case
    if index == len(values):
        if current_res == target:
            return ops
        return False
    current_number = values[index]
    # ADD
    add_path = compute_operations(target, values, current_res + current_number, index + 1, ops + [f"+{current_number}"])

    # if a + is found return it
    if add_path:
        return add_path

    # MULTIPLY
    mult_path = compute_operations(target, values, current_res * current_number, index + 1,
                                   ops + [f"x{current_number}"])

    # if a * is found return it
    if mult_path:
        return mult_path


def bridge_repair(data):
    res = 0
    for element in data:
        test_val, values = element
        ops = compute_operations(test_val, values)
        print(ops)
        if ops:
            res += test_val
    return res


if __name__ == "__main__":
    testInput = "./test.txt"
    realInput = "../data/2024/day7Input.txt"

    data = read_file(realInput)
    print(bridge_repair(data))

# first output: 2437272016585
