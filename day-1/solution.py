# solution
# read text file
# read each column in text file into two sorted lists
# find pairwise different between the lists and add the difference
# that's the total distance between the two lists

def get_total_distance(filename):
    list1 = []
    list2 = []

    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            list1.append(int(values[0]))
            list2.append(int(values[1]))
    list1.sort()
    list2.sort()
    total_dist = 0

    for val1, val2 in zip(list1, list2):
        total_dist += abs(val1 - val2)

    return total_dist

total = get_total_distance("input.txt")
print(total)