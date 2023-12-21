
def find_original_set(*args):
    if len(args) != 97:
        raise ValueError("Exactly 97 arguments expected")

    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)

    return original_set
