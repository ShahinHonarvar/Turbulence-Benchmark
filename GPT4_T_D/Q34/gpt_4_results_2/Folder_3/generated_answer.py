
def find_original_set(*args):
    if len(args) != 59:
        raise ValueError("Number of arguments must be exactly 59.")
    original_set = set()
    for subset in args:
        if not isinstance(subset, set):
            raise ValueError("Each argument must be a set.")
        original_set.update(subset)
    return original_set
