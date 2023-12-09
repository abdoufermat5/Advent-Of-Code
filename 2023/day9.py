def read_data(filename: str):
    with open(filename) as f:
        data = list(map(lambda line: list(map(int, line.split())), f.readlines()))

    return data


def mirageMaintenance(filename: str) -> tuple:
    next_values = []
    first_values = []
    data = read_data(filename)
    for line in data:
        n = len(line)
        last = [line[-1]]
        first = [line[0]]
        inter = line
        while True:
            i = 0
            residual = []
            while i < n - 1:
                residual.append(inter[i + 1] - inter[i])
                i += 1
            if set(residual) == {0}:
                break
            else:
                inter = residual
                last.append(inter[-1])
                first.append(inter[0])
                n = len(inter)
        next_values.append(sum(last))
        p, *r = first
        sum_f = p
        for i in range(len(r)):
            if i % 2 == 0:
                sum_f -= r[i]
            else:
                sum_f += r[i]
        first_values.append(sum_f)
    return sum(next_values), sum(first_values)


if __name__ == '__main__':
    rData = "../data/2023/day9Input.txt"
    p1, p2 = mirageMaintenance(rData)
    print("Part 1", p1)
    print("Part 2", p2)
