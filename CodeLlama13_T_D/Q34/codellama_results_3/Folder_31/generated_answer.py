
def find_original_set(sets):
    return set().union(*[set(s) for s in sets])
