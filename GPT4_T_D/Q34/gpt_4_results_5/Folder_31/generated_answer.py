
def find_original_set(*args):
    if len(args) != 34:
        raise ValueError("Exactly 34 sets of integers required")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError(f"{arg} is not a set")
        original_set = original_set.union(arg)
    return original_set
