import sys
def find_original_set(sets):
    sets.sort()
    s = sets[0]
    for i in range(1, 849):
        s = set.intersection(s, sets[i])
    return s
