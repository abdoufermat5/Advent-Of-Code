def winRange(t, d):
    firstWin = 1
    while firstWin < t // 2:
        if firstWin * (t - firstWin) > d:
            break
        firstWin += 1
    return t - 2 * firstWin


def waitForIt(filename: str) -> int:
    product = 1
    with open(filename) as f:
        time, distance = [list(map(int, l.split(":")[1].split())) for l in f.readlines()]
        for i in range(len(time)):
            t, d = time[i], distance[i]
            product *= winRange(t, d)
    return product


def waitForIt2(filename: str) -> int:
    with open(filename) as f:
        time, distance = [int(l.split(":")[1].replace(" ", "")) for l in f.readlines()]
    return winRange(time, distance)


if __name__ == "__main__":
    rData = "../data/2023/day6Input.txt"
    print(waitForIt2(rData))
