
def find_original_set(*args):
    if len(args) != 162:
        raise ValueError("Requires exactly 162 arguments")
    all_sets = set()
    for arg in args:
        all_sets = all_sets.union(arg)
    return all_sets
