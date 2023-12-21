
def find_original_set(*args):
    if len(args) != 96:
        raise ValueError("Exactly 96 arguments are required.")
    original_set = set.union(*args)
    return original_set
