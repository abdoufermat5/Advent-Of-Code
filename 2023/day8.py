def read_data(filename: str):
    import re
    tuple_pattern = re.compile(r'\(([0-9A-Z]+),\s*([0-9A-Z]+)\)')
    with open(filename) as f:
        instructions, _, *data = f.read().split("\n")
        node_repo = {
            line.split("=")[0].strip(): {"L": tuple_pattern.findall(line)[0][0], "R": tuple_pattern.findall(line)[0][1]}
            for line in data}
    return instructions, node_repo


def get_all_mode_end_by(node_repo: dict, end: str = "A") -> list:
    all_a = []
    for node in node_repo.keys():
        if node[-1] == end:
            all_a.append(node)
    return all_a


def find_num_steps(instructions, node_repo, start: str = "AAA", target: str = "Z", target_count: int = 3):
    num_step = 0

    current = start
    while current.count(target) != target_count and current[-1] != target:
        m = instructions[num_step % len(instructions)]
        current = node_repo[current][m]
        num_step += 1

    return num_step


def hauntedWasteland1(filename: str) -> int:
    instructions, node_repo = read_data(filename)

    num_step = find_num_steps(instructions, node_repo)

    return num_step


def hauntedWasteland2(filename: str) -> int:
    num_steps = []
    target = "Z"

    instructions, node_repo = read_data(filename)
    start = get_all_mode_end_by(node_repo)
    for el in start:
        num_steps.append(find_num_steps(instructions, node_repo, el, target, 1))
    import math
    # we need to compute the lcm to know when all the starting node reach an end-by-Z node
    lcm = math.lcm(*num_steps)
    return lcm


if __name__ == "__main__":
    rData = "../data/2023/day8Input.txt"
    print("Part 1: ", hauntedWasteland1(rData))
    print("Part 2: ", hauntedWasteland2(rData))
