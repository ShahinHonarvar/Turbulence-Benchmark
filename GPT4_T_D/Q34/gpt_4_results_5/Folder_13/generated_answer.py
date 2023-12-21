
def find_original_set(*args):
    if len(args) != 845:
        raise ValueError("Wrong number of parameters")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
