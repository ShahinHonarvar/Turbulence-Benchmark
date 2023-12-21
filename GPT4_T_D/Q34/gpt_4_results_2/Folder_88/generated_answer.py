
def find_original_set(*args):
    if len(args) != 27:
        raise ValueError("The number of arguments should be exactly 27")
    original_set = set().union(*args)
    return original_set
