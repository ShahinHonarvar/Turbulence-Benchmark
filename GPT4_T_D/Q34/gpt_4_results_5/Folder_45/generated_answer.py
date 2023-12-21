
def find_original_set(*args):
    if len(args) != 97:
        raise ValueError("Function requires 97 distinct sets of integers")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
