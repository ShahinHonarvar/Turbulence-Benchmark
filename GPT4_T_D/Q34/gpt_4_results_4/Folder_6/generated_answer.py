
def find_original_set(*args):
    if len(args) != 276:
        raise ValueError("Function requires exactly 276 sets.")
    original_set = set.union(*args)
    return original_set
