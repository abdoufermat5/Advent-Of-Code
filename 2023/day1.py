def trebuchet(filename: str) -> int:
    with open(filename) as f:
        data = f.readlines()

    import re
    alpha_to_digit = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9,
        # restant
        "2ne": 21, "8wo": 82, "8hree": 83, "5ight": 58,
        "1ight": 18, "7ine": 79, "3ight": 38, "9ight": 98
    }

    num_pattern = re.compile(r"\d")
    pairs = []

    for el in data:
        convert = re.sub(r'(one|two|three|four|five|six|seven|eight|nine)',
                         lambda match: str(alpha_to_digit[match.group(0)]), el.lower())
        second_convert = re.sub(r'(2ne|8wo|8hree|5ight|1ight|7ine|3ight|9ight)',
                                lambda match: str(alpha_to_digit[match.group(0)]), convert)
        digits = num_pattern.findall(second_convert)
        if len(digits) > 0:
            pairs.append(int(digits[0] + digits[-1]))
    return sum(pairs)


result = trebuchet("./data/day1Input.txt")
print(result)
