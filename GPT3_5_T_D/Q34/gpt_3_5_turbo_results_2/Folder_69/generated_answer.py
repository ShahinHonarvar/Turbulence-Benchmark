
def find_original_set(*sets):
    if len(sets) == 0:
        return set()
    original_set = sets[0]
    for s in sets[1:]:
        original_set = original_set.union(s)
    return original_set
