
def find_original_set(*args):
    if len(args) != 35:
        raise ValueError("Exactly 35 arguments are expected.")
    original_set = set().union(*args)
    return original_set
