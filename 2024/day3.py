import re


def read_file(file_path: str) -> list:
    with open(file_path, "r") as f:
        return f.readlines()


def mul(a, b):
    return a * b


def match_mul(s, v2=False):
    if v2:
        pattern = r"don\'t\(\)|mul\(\d{1,3},\d{1,3}\)|do\(\)"
        r = re.compile(pattern).findall(s)
        return r

    else:
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        res = re.compile(pattern).findall(s)
        return res


def compute_mul(line, v2=False):
    res = 0
    if v2:
        f = True
        for el in line:
            if el == "do()":
                f = True
            elif el == "don't()":
                f = False
            else:
                if f:
                    res += eval(el)
    else:
        for el in line:
            res += eval(el)
    return res


def mull_it_over_1(input_data, v2=False):
    p_input_list = []
    for line in input_data:
        patterns_list = match_mul(line, v2)
        p_input_list += patterns_list
    res = compute_mul(p_input_list, v2)
    return res


if __name__ == "__main__":
    testInput = "./test.txt"
    realInput = "../data/2024/day3Input.txt"

    data = read_file(realInput)

    print(mull_it_over_1(data))
    print(mull_it_over_1(data, v2=True))

# first output: 188741603
# second output: 67269798
