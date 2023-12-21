
def find_original_set(*args):
    if len(args) != 37:
        raise ValueError("This function requires exactly 37 distinct sets of integers as arguments.")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
