## Part 1
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
print("total_distance", total)

## Part 2
# read column 1 as list 1
# read column2 as frequency dict where you know how many times each item appears in list 2
# iterate over list 1 and multiply it by the item's frequency and add them all
# that's the total similarity of two lists

def get_similarity(filename):
    list1 = []
    item2freq = {}

    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            list1.append(int(values[0]))
            item2 = int(values[1])
            if item2 in item2freq:
                item2freq[item2] += 1
            else:
                item2freq[item2] = 1

    similarity_score = 0
    for item in list1:
        similarity_score += (item * item2freq.get(item, 0))
    
    return similarity_score

sim_score = get_similarity("input.txt")
print("similarity_score", sim_score)