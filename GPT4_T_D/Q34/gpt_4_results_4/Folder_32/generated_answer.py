
def find_original_set(*args):
    if len(args) != 459:
        raise ValueError("Exactly 459 arguments are required")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
