import re
def find_pattern(input):
    with open(input, "r") as file:
        content = file.read()
    pattern = r"mul\(\d+,\d+\)"

    matches = re.findall(pattern, content)

    return matches

def calculations(mul_list):
    total_sum = 0
    for item in mul_list:
        numbers = re.findall(r"\d+", item)
        mul = int(numbers[0]) * int(numbers[1])
        total_sum+=mul
    return total_sum

matches = find_pattern("input.txt")
total_sum = calculations(matches)
print(total_sum)