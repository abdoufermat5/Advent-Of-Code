class Node:
    def __init__(self, position, min_dist=0, name="S"):
        self.position = position
        self.min_dist = min_dist
        self.name = name
        self.prev = None

    def __str__(self):
        return f"Node(position={self.position}, min_dist={self.min_dist}, name={self.name})"

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.position < other.position

    def __gt__(self, other):
        return self.position > other.position

    def __hash__(self):
        return hash(self.position)


DIRECTION = {
    "E": (0, 1),
    "W": (0, -1),
    "N": (-1, 0),
    "S": (1, 0)
}

# Rules
R = {
    "|": [DIRECTION["N"], DIRECTION["S"]],
    "-": [DIRECTION["E"], DIRECTION["W"]],
    "L": [DIRECTION["N"], DIRECTION["E"]],
    "J": [DIRECTION["N"], DIRECTION["W"]],
    "7": [DIRECTION["S"], DIRECTION["W"]],
    "F": [DIRECTION["S"], DIRECTION["E"]],
    "S": [DIRECTION["E"], DIRECTION["W"], DIRECTION["N"], DIRECTION["S"]]
}


def pipeMaze(filename: str) -> int:
    with open(filename) as f:
        data = f.read().split("\n")
        n_row = len(data)
        n_col = len(data[0])
        current = []
        tracks = set()

        for i in range(n_row):
            for j in range(n_col):
                if data[i][j] == "S":
                    source = Node((i, j), 0, name="S")
                    for x, y in DIRECTION.values():
                        if 0 <= i + x < n_row and 0 <= j + y < n_col:
                            if data[i + x][j + y] != ".":
                                node = Node((i + x, j + y), 1, data[i + x][j + y])
                                node.prev = source.position
                                current.append(node)
                    break

        current = current[0]

        while current.name != "S":
            tracks.add(current)
            i, j = current.position
            min_distance = current.min_dist
            name = current.name
            prev_node_pos = current.prev
            next_node = [Node((x + i, y + j), min_distance + 1, data[x + i][y + j]) \
                         for (x, y) in R[name] if (x + i, y + j) != prev_node_pos][0]
            next_node.prev = current.position
            current = next_node

        return current.min_dist//2


if __name__ == "__main__":
    tData = "./test.txt"
    rData = "../data/2023/day10Input.txt"
    # part 1: 7145
    print("Part 1: ", pipeMaze(rData))
