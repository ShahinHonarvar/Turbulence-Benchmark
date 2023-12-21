
def find_original_set(*args):
    if len(args) != 77:
        raise ValueError("Requires exactly 77 arguments")
    original_set = set().union(*args)
    return original_set
