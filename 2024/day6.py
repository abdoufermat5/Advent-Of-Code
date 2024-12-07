GO_TO = {
    "^": ">",
    "v": "<",
    "<": "^",
    ">": "v"
}


def read_file(file_path: str):
    d = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            d.append(list(line))
    return d


def get_nodes_and_init_pos(grid):
    nodes = {}
    man = None
    for i in range(len(grid)):
        line = grid[i]
        for j in range(len(line)):
            if grid[i][j] == "#":
                nodes[(i, j)] = "#"
            if grid[i][j] in GO_TO.keys():
                man = (i, j, grid[i][j])
    return nodes, man


def move(i, j, direction):
    if direction == "^":
        return i - 1, j
    if direction == "<":
        return i, j - 1
    if direction == ">":
        return i, j + 1
    if direction == "v":
        return i + 1, j


def track_man_pos(i, j, direction):
    man_pos = None
    if direction == "^":
        i, j = i + 1, j
        new_direction = GO_TO["^"]
        man_pos = (i, j, new_direction)
    if direction == "<":
        i, j = i, j + 1
        new_direction = GO_TO["<"]
        man_pos = (i, j, new_direction)
    if direction == ">":
        i, j = i, j - 1
        new_direction = GO_TO[">"]
        man_pos = (i, j, new_direction)
    if direction == "v":
        i, j = i - 1, j
        new_direction = GO_TO["v"]
        man_pos = (i, j, new_direction)
    return man_pos


def guard_gallivant(data):
    n = len(data)
    m = len(data[0])
    nodes, man = get_nodes_and_init_pos(data)
    tracks = set()
    i, j, direction = man
    while 0 <= i < n and 0 <= j < m:
        while 0 <= i < n and 0 <= j < m and (i, j) not in nodes:
            tracks.add((i, j))
            i, j = move(i, j, direction)
        if not (0 <= i < n and 0 <= j < m):
            break

        i, j, direction = track_man_pos(i, j, direction)
    return len(tracks)


if __name__ == "__main__":
    testInput = "./test.txt"
    realInput = "../data/2024/day6Input.txt"
    data = read_file(realInput)
    print(guard_gallivant(data))

# first output: 4569
# second output: 6456
