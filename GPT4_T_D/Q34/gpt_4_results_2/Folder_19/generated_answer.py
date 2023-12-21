
def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('23 sets of integers required')
    original_set = set()
    for a in args:
        original_set.update(a)
    return original_set
