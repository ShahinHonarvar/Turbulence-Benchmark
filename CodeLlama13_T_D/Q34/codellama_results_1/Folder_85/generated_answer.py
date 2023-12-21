
def find_original_set(*args):
    sets = set(map(set, args))
    return min(sets, key=len)
