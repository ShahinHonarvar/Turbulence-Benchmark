
def find_original_set(*args):
    if len(args) != 68:
        raise ValueError("Exactly 68 arguments expected")
    original_set = set()
    for set_i in args:
        original_set = original_set.union(set_i)
    return original_set
