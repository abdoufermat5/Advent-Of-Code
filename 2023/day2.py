def cubeConundrum1(filename: str) -> int:
    cond = {"green": 13, "red": 12, "blue": 14}
    ids_sum = 0
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            # get game number and list of subset
            g, c = line.split(":")
            # split subsets
            subsets = c.split(";")
            is_oks = True
            for p in subsets:
                q = p.replace(",", "").strip().split()
                d = {}
                for i in range(0, len(q), 2):
                    d[q[i + 1]] = int(q[i])

                for color in cond:
                    is_oks = is_oks and cond[color] >= d.get(color, 0)
            # check if all subset meet requirements
            if is_oks:
                ids_sum += int(g.split()[-1])
    return ids_sum


def cubeConundrum2(filename: str) -> int:
    powers_sum = 0
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            g, c = line.split(":")

            q = c.replace(";", "").replace(",", "").strip().split()
            max_val = {}
            for i in range(0, len(q), 2):
                if q[i + 1] in max_val:
                    max_val[q[i + 1]] = max(int(q[i]), max_val[q[i + 1]])
                else:
                    max_val[q[i + 1]] = int(q[i])
            p = 1
            for el in max_val.values():
                p *= el
            powers_sum += p
    return powers_sum
