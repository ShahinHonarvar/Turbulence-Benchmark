
def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Expected 276 arguments')
    return set.union(*args)
