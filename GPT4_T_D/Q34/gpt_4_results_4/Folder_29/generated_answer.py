
def find_original_set(*args):
    original_set = set()
    if len(args) == 94:
        for current_set in args:
            original_set = original_set.union(current_set)
    return original_set
