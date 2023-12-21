
def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Exactly 72 sets of integers are required')
    return set.union(*args)
