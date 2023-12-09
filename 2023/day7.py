from collections import Counter

handType = {
    "fiveOfAKind": lambda x: 7 if len(set(x)) == 1 else False,
    "fourOfAKind": lambda x: 6 if set(Counter(x).values()) == {4, 1} else False,
    "fullHouse": lambda x: 5 if set(Counter(x).values()) == {3, 2} else False,
    "threeOfAKind": lambda x: 4 if set(Counter(x).values()) == {3, 1} else False,
    "twoPair": lambda x: 3 if sorted(list(Counter(x).values())) == [1, 2, 2] else False,
    "onePair": lambda x: 2 if sorted(list(Counter(x).values())) == [1, 1, 1, 2] else False,
    "highCard": lambda x: 1 if list(Counter(x).values()) == [1, 1, 1, 1, 1] else False
}

cardMap = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def getType(h):
    for hand in handType.keys():
        if handType[hand](h):
            return handType[hand](h)


def getValue(h):
    s = []
    for c in h:
        s.append(int(cardMap.get(c, c)))
    return s


def increaseValue(h):
    pass


def camelCards(filename: str) -> int:
    total = 0
    with open(filename) as f:
        data = f.readlines()
        hands = []
        for line in data:
            h, v = line.strip().split()
            hands.append((h, getType(h), getValue(h), int(v)))

    hands.sort(key=lambda x: (x[1], *x[2]))

    for (i, h) in enumerate(hands):
        total += h[-1] * (i + 1)
    return total


if __name__ == '__main__':
    tData = "./test.txt"
    rData = "../data/2023/day7Input.txt"

    print(camelCards(tData))
