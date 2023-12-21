
def find_original_set(*args):
    if len(args) != 54:
        raise ValueError("Exactly 54 arguments expected")
    original_set = set()
    for current_set in args:
        original_set.update(current_set)
    return original_set
