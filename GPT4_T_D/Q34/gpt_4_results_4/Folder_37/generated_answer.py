
def find_original_set(*args):
    if len(args) != 67:
        raise ValueError("Exactly 67 arguments expected")

    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)

    return original_set
