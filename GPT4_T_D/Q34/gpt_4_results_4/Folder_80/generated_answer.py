
def find_original_set(*args):
    original_set = set()
    if len(args) != 453:
        raise ValueError('Wrong number of arguments, expected 453')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments should be sets')
        original_set.update(arg)
    return original_set
