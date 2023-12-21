
def find_original_set(*args):
    if len(args) != 453:
        raise ValueError("Must provide exactly 453 distinct arguments.")
    original_set = set()
    for curr_set in args:
        original_set = original_set.union(curr_set)
    return original_set
