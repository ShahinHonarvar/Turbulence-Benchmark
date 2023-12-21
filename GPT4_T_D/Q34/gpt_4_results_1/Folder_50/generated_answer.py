
def find_original_set(*args):
    if len(args) != 99:
        raise ValueError("Function requires exactly 99 sets.")
    else:
        original_set = set()
        for arg in args:
            if isinstance(arg, set):
                original_set = original_set.union(arg)
    return original_set
