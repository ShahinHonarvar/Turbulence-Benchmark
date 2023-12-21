
def find_original_set(*args):
    original_set = set()
    for ind_set in args:
        original_set = original_set.union(ind_set)

    return original_set
