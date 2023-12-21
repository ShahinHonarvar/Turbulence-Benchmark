
def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Expected exactly 96 arguments')

    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be of type set')

        original_set = original_set.union(arg)

    return original_set
