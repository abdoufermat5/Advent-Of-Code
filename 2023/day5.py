import sys
def seedFertilizer(filename: str) -> int:
    from collections import defaultdict
    with open(filename) as f:
        data = f.readlines()
        seeds = list(map(int, data[0].strip().split(':')[1].split()))
        sourceCategory, targetCategory = "", ""
        repos = defaultdict(dict)
        repos["seed"] = {s: s for s in seeds}
        for line in data[1:]:
            if not line.strip():
                sourceCategory, targetCategory = "", ""
            elif not sourceCategory:
                tmp = line.strip().split(' ')[0].split("-")
                sourceCategory, targetCategory = tmp[0], tmp[-1]
                if targetCategory not in repos:
                    repos[targetCategory] = {}
            else:
                targetInit, sourceInit, rLength = map(int, line.strip().split(' '))

                repos[targetCategory].update(
                    {
                        s: targetInit + s - sourceInit \
                            if s >= sourceInit \
                               and targetInit + s - sourceInit < targetInit + rLength \
                            else repos[targetCategory].get(s, s) \
                        for s in repos[sourceCategory].values()}
                )
        for k in repos.keys():
            print(k, *repos[k].values())
        return min(repos["location"].values())


if __name__ == '__main__':
    rData = "../data/2023/day5Input.txt"
    print(seedFertilizer(rData))
