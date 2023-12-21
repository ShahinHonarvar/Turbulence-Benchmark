
def find_original_set(*args):
    if len(args) != 72:
        raise ValueError("Incorrect number of arguments. Expected 72 sets.")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
