
def find_original_set(sets):
    return set().union(*[frozenset({i}) for i in sets])
