
def find_original_set(*args):
    if len(args) != 92:
        raise Exception('Number of arguments must be equal to 92.')

    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise Exception('Each argument must be a set.')
        original_set.update(arg)

    return original_set
