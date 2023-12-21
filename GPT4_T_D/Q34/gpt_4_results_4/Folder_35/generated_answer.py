
def find_original_set(*args):
    if len(args) != 702:
        raise ValueError("Exactly 702 arguments are expected.")
    return set.union(*args)
