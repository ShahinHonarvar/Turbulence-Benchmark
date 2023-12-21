
def find_original_set(*args):
    if len(args) != 84:
        raise ValueError("Exactly 84 distinct arguments are required.")
    original_set = set()
    for arg in args:
        original_set |= arg

    return original_set
