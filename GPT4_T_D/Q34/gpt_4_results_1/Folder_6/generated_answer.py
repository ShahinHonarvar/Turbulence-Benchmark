
def find_original_set(*args):
    if len(args) != 276:
        raise ValueError("The function should take exactly 276 arguments.")
    original_set = set()
    for a in args:
        original_set |= a
    return original_set
