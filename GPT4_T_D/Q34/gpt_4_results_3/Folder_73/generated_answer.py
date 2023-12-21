
def find_original_set(*args):
    if len(args) != 19:
        raise ValueError('The number of arguments must be 19.')
    original_set = set.union(*args)
    return original_set
