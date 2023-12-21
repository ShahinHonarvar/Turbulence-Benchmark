
def find_original_set(sets):
    return set().union(*[set(x) for x in sets])
