
def find_original_set(*sets):
    original_set = sets[0]
    for set in sets:
        original_set = original_set.union(set)
    return original_set
