
def find_original_set(*args):
    if len(args) != 38:
        raise ValueError("Exactly 38 sets are required.")

    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)

    return original_set
