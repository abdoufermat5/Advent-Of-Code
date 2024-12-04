def read_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        return lines


def get_neighbour_vd(matrix, i, j):
    vert = []
    diag = []
    # t-d and bl-tr and br-tl
    if i - 3 >= 0:
        v = matrix[i - 1][j] + matrix[i - 2][j] + matrix[i - 3][j]
        if v == "MAS":
            vert.append(v)
        if j + 3 < len(matrix[i]):
            d = matrix[i - 1][j + 1] + matrix[i - 2][j + 2] + matrix[i - 3][j + 3]
            if d == "MAS":
                diag.append(d)
        if j - 3 >= 0:
            d = matrix[i - 1][j - 1] + matrix[i - 2][j - 2] + matrix[i - 3][j - 3]
            if d == "MAS":
                diag.append(d)
    if i + 3 < len(matrix):
        v = matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 3][j]
        if v == "MAS":
            vert.append(v)
        if j + 4 < len(matrix[i]):
            d = matrix[i + 1][j + 1] + matrix[i + 2][j + 2] + matrix[i + 3][j + 3]
            if d == "MAS":
                diag.append(d)
        if j - 3 >= 0:
            d = matrix[i + 1][j - 1] + matrix[i + 2][j - 2] + matrix[i + 3][j - 3]
            if d == "MAS":
                diag.append(d)
    return vert, diag


def ceres_search(data, v2=False):
    n = len(data)
    res = 0
    if v2:
        for i in range(n):
            for j in range(len(data[i])):
                if data[i][j] == "A":
                    if i - 1 >= 0 and j - 1 >= 0 and j + 1 < len(data[i]) and i + 1 < len(data[i]):
                        t = data[i - 1][j - 1] + data[i - 1][j + 1]
                        b = data[i + 1][j - 1] + data[i + 1][j + 1]
                        if t == b and (b == "SM" or b == "MS"):
                            res += 1
                        if (t == "SS" and b == "MM") or (t == "MM" and b == "SS"):
                            res += 1
    else:
        _neighbours = []
        for j in range(n):
            line = data[j]
            for i in range(len(line)):
                if line[i] == "X":
                    # get horiz neighbour
                    if i - 3 >= 0:
                        _neighbours.append(line[i - 3:i][::-1])
                    if i + 3 < len(line):
                        _neighbours.append(line[i + 1:i + 4])
                    vert, diag = get_neighbour_vd(data, j, i)
                    _neighbours.extend(vert)
                    _neighbours.extend(diag)
        res = _neighbours.count("MAS")
    return res


if __name__ == "__main__":
    testInput = "./test.txt"
    realInput = "../data/2024/day4Input.txt"

    data = read_file(realInput)

    print(ceres_search(data))
    print(ceres_search(data, v2=True))

# first output: 2358
# second output: 1737
