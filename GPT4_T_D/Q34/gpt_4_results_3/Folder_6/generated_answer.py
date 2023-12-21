
def find_original_set(*args):
    if len(args) != 276:
        raise ValueError("Expected 276 distinct argument sets")
    return set().union(*args)
