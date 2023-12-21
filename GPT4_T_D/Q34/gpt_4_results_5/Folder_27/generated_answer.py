
def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Function requires exactly 100 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument should be a set')
        original_set = original_set.union(arg)
    return original_set
