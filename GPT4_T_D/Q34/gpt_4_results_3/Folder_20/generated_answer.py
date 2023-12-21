
def find_original_set(*args):
    if len(args) != 66:
        raise ValueError("Requires exactly 66 arguments")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
