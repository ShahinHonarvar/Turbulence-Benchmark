
def find_original_set(*args):
    if len(args) != 990:
        raise ValueError("Exactly 990 arguments required")
    original_set = set()
    for curr_set in args:
        original_set.update(curr_set)
    return original_set
