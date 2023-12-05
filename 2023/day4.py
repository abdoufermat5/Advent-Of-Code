def scratchCards1(filename: str) -> int:
    total_sum = 0
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            cardId, cards = line.strip().split(":")
            wCard, pCard = cards.strip().split("|")
            nbPwCard = len(set(wCard.split()).intersection(set(pCard.split())))
            if nbPwCard > 1:
                total_sum += 2 ** (len(set(wCard.split()).intersection(set(pCard.split()))) - 1)
            else:
                total_sum += nbPwCard
    return total_sum


def scratchCards2(filename: str) -> int:
    from collections import defaultdict

    instances = defaultdict(int)
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            cardId, cards = line.strip().split(":")
            cardId = int(cardId.split()[-1])
            if cardId not in instances:
                instances[cardId] = 1
            else:
                instances[cardId] += 1
            wCard, pCard = cards.strip().split("|")
            nbPwCard = len(set(wCard.split()).intersection(set(pCard.split())))
            if nbPwCard >= 1:
                for i in range(cardId + 1, cardId + nbPwCard + 1):
                    if i in instances:
                        instances[i] += instances[cardId]
                    else:
                        instances[i] = instances[cardId]
    return sum(instances.values())
