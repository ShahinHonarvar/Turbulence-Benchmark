
def find_original_set(*args):
    if len(args) != 20:
        raise ValueError("Expecting 20 arguments")
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set
