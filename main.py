def map_number(number, mapping):
    for destination_start, source_start, length in mapping:
        if source_start <= number < source_start + length:
            return destination_start + (number - source_start)
    return number

def process_seed(seed, mappings):
    for mapping in mappings:
        seed = map_number(seed, mapping)
    return seed

def read_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    sections = content.split('\n\n')
    print(sections)
    seeds_section = sections[0]
    seed_ranges = [(int(x), int(y)) for x, y in (pair.split() for pair in seeds_section.split(': ')[1].split(','))]

    mappings = []
    for section in sections[1:]:
        mapping = [tuple(map(int, line.split())) for line in section.split('\n')[1:]]
        mappings.append(mapping)

    return seed_ranges, mappings

def solve_advent_of_code(file_path):
    seed_ranges, mappings = read_input(file_path)

    seeds = []
    for start, length in seed_ranges:
        seeds.extend(range(start, start + length))

    locations = [process_seed(seed, mappings) for seed in seeds]

    return min(locations)


if __name__ == '__main__':
    file_path = './data/2023/day5Input.txt'
    print(solve_advent_of_code(file_path))
