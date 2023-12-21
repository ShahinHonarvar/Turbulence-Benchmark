import itertools
def find_original_set(s):
    sets = {s}
    for i in range(1,53):
        for s in itertools.combinations(sets,i):
            if all(a in s for a in s):
                sets.add(s)
    return min(sets)
