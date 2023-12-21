
def find_original_set(args):
    sets = set(map(lambda x: frozenset(x), args))
    original_set = sets.pop()
    while sets:
        new_set = sets.pop()
        if not new_set <= original_set:
            original_set |= new_set
    return list(original_set)
