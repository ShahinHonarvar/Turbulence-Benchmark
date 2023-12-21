import sys
def find_original_set(sets):
    # sort by size
    sets = sorted(sets, key=lambda s: len(s))
    # find largest common subset
    s = sets[0]
    for i in range(1, len(sets)):
        s &= sets[i]
    return s
