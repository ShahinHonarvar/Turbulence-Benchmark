
def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Function accepts exactly 72 distinct sets as arguments.')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
