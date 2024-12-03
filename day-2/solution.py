
def is_safe_report(levels):
    decreasing = levels[1] < levels[0]
    safe = True
    for i in range(len(levels) - 1):
        diff = abs(int(levels[i]) - int(levels[i+1]))
        if diff <= 0 or diff > 3:
            safe = False
            continue
        if decreasing and levels[i] < levels[i+1]:
            safe = False
            continue
        if not decreasing and levels[i] > levels[i+1]:
            safe = False
            continue
    return safe

def is_safe(filename):
    assessment = []
    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            safe = is_safe_report(levels)
            assessment.append(safe)
    return assessment


def is_safe_with_dampner(filename):
    assessment = []
    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if is_safe_report(levels):
                assessment.append(True)
                continue
            dampner_safe = False
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i+1:]
                if is_safe_report(modified_levels):
                    dampner_safe = True
                    break
            assessment.append(dampner_safe)

    return assessment


assessments = is_safe("input.txt")
safe_counts = 0
for assess in assessments:
    if assess == True:
        safe_counts+=1
print(safe_counts)



assessments = is_safe_with_dampner("input.txt")
safe_counts = 0
for assess in assessments:
    if assess == True:
        safe_counts+=1
print(safe_counts)