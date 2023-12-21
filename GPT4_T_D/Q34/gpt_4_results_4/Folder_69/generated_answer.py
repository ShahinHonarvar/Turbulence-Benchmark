
def find_original_set(*args):
    if len(args) != 126:
        raise ValueError("This function requires exactly 126 arguments.")
    original_set = set().union(*args)
    return original_set
