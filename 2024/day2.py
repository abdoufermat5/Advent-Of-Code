MIN_DIFF, MAX_DIFF = 1, 3


def get_occurrences(arr: list) -> list:
    occ = {}
    for num in arr:
        if num in occ:
            occ[num] += 1
        else:
            occ[num] = 1
    return list(occ.values())


def test_increasing(arr: list) -> bool:
    for i in range(1, len(arr)):
        if MIN_DIFF <= arr[i] - arr[i - 1] <= MAX_DIFF:
            pass
        else:
            return False
    return True


def test_decreasing(arr: list) -> bool:
    for i in range(1, len(arr)):
        if MIN_DIFF <= arr[i - 1] - arr[i] <= MAX_DIFF:
            pass
        else:
            return False
    return True


def line_check(line: list) -> bool:
    if line[0] < line[1]:
        check = test_increasing(line)
        return check
    # all decreasing
    else:
        check = test_decreasing(line)
        return check


def red_nosed_reports_1(input_data: list[bool]) -> int:
    return sum(input_data)


def red_nosed_reports_2(input_data):
    # get previous result
    res = 0
    # check rest
    for line in input_data:
        for j in range(1, len(line)):
            # if by removing i or i-1 the condition are satisfied then we're good
            is_ok = (test_increasing(line[:j] + line[j + 1:]) or test_decreasing(line[:j] + line[j + 1:])) or \
                    (test_increasing(line[:j - 1] + line[j:]) or test_decreasing(line[:j - 1] + line[j:]))
            if is_ok:
                res += 1
                break

    return res


def read_file(file_path: str) -> list[list]:
    res = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            i_res = map(int, line.split())
            res.append(list(i_res))
    return res


if __name__ == "__main__":
    testInput = "./test.txt"
    realInput = "../data/2024/day2Input.txt"

    data = read_file(realInput)
    line_checked_data = [line_check(line) for line in data]
    print(red_nosed_reports_1(line_checked_data))
    print(red_nosed_reports_2(data))

# first output: 624
# second output: 658
