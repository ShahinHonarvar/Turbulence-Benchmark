
def find_original_set(*args):
    if len(args) != 21:
        raise ValueError("Exactly 21 arguments are expected")
    original_set = set.union(*args)
    return original_set
