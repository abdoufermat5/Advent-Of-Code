def partition(A, l, r):
    x = A[r]
    i = l - 1

    for j in range(l, r):
        if A[j] <= x:
            i += 1
            t = A[j]
            A[j] = A[i]
            A[i] = t
    # excahnge the element at i+1 A[i+1] with the rightmost element A[r]
    A[r] = A[i + 1]
    A[i + 1] = x
    return i + 1


def quicksort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quicksort(A, l, p - 1)
        quicksort(A, p + 1, r)


def get_occurrences(sroted_arr):
    occ = {}
    for num in sroted_arr:
        if num in occ:
            occ[num] += 1
        else:
            occ[num] = 1
    return occ


def historian_hysteria_1(first: list, second: list) -> int:
    res = 0
    for i in range(len(first)):
        res += abs(first[i] - second[i])
    return res


def historian_hysteria_2(first: list, second: dict) -> int:
    res = 0
    for el in first:
        res += el * second.get(el, 0)
    return res


if __name__ == '__main__':
    real_input = "../data/2024/day1Input.txt"
    test_input = "./test.txt"
    first = []
    second = []
    with open(real_input, "r") as input_data:
        lines = input_data.readlines()
        for l in lines:
            L = l.split()
            first.append(int(L[0]))
            second.append(int(L[1]))
    quicksort(first, 0, len(first) - 1)
    quicksort(second, 0, len(second) - 1)
    # occurrence dict in second list (already sorted)
    occ_second = get_occurrences(second)

    print(historian_hysteria_1(first, second))
    print(historian_hysteria_2(first, occ_second))

# first output: 1590491
# second output: 22588371
