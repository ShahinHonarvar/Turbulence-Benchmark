
def find_original_set(*args):
    if len(args) != 537:
        raise ValueError("547 distinct arguments are expected")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
