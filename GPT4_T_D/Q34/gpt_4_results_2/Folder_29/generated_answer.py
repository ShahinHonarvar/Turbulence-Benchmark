
def find_original_set(*args):
    if len(args) != 94:
        raise ValueError('Number of arguments must be exactly 94!')
    return set.union(*args)
