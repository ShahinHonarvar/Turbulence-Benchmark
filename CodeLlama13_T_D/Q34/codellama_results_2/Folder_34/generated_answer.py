
def find_original_set(*args):
    sets = list(args)
    while len(sets) > 1:
        new_set = set()
        for s in sets:
            new_set |= s
        sets = [new_set]
    return sets[0]
