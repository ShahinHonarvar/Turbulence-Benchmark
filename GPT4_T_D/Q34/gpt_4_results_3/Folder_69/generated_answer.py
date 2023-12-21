
def find_original_set(*args):
    if len(args) != 126:
        raise ValueError("Exactly 126 arguments are required")
    return set.union(*args)
