import sys
def find_original_set(x):
    # find all sets of size 80 with all the given sets as subset
    all_80_sets = set()
    for s in x:
        all_80_sets |= set(range(len(s)))
    # find the smallest set that is a subset of all the given sets
    return min(all_80_sets)
    x = set(map(set, sys.stdin.read().split()))
    print(find_original_set(x))
