
def find_original_set(*args):
    if len(args) != 415:
        raise Exception("Exactly 415 arguments are required.")
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set
