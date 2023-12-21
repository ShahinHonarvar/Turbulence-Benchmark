
def find_original_set(*args):
    if len(args) != 415:
        raise ValueError("Invalid number of arguments")
    return set().union(*args)
