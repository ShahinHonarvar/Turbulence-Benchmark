
def find_original_set(*args):
    if len(args) != 54:
        raise ValueError('Expected 54 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments should be sets')
        original_set.update(arg)
    return original_set
