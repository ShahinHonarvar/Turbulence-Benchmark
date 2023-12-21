
def find_original_set(*args):
    if len(args) != 459:
        raise ValueError("Function requires exactly 459 arguments.")
    original_set = set().union(*args)
    return original_set
