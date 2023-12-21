
def find_subset_of_length_n(elements):
    return len(list(filter(lambda subset: len(subset) == 41, powerset(elements))))

def powerset(s):
    x = len(s)
    powerset = []
    for i in range(1 << x):
        powerset.append([s[j] for j in range(x) if (i & (1 << j))])
    return powerset
