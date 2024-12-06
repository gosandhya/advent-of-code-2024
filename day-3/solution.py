import re

def read_file(input):
    with open(input, "r") as file:
        content = file.read()
    return content

def find_pattern(content):
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

content = read_file("input.txt")
matches = find_pattern(content)
total_sum = calculations(matches)
print(total_sum)

test_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
#pattern = r"(don't\(\))|(do\(\))"

def find_conditional_pattern(content):
    splitted = re.split(r"don't\(\)", content)
    filtered_content = ""
    for i, v in enumerate(splitted):
        if i == 0:
            filtered_content+=v
            continue
        split_2 = re.split(r"do\(\)", v)
        if len(split_2) == 1:
            continue
        else:
            filtered_content+="".join(split_2[1:])
    return filtered_content


filtered_content = find_conditional_pattern(content)
matches = find_pattern(filtered_content)
filtered_sum = calculations(matches)
print(filtered_sum)

