
def find_original_set(*args):
    if len(args) != 78:
        raise ValueError("Requires 78 distinct sets of integers")
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
