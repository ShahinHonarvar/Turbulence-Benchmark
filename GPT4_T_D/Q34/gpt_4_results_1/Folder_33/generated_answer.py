
def find_original_set(*args):
    if len(args) != 263:
        raise ValueError('Function is expected to take exactly 263 arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments should be of type set.')
        original_set.update(arg)
    return original_set
