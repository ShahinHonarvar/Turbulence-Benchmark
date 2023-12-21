import itertools
def find_original_set(arg):
    return {*min(set(s) for s in arg),}
