
def find_original_set(args):
    sets = set()
    for arg in args:
        sets |= set(arg)
    return sets
