
def find_original_set(*args):
    if len(args) != 312:
        raise ValueError("Function requires exactly 312 arguments!")

    original_set = set().union(*args)

    return original_set
