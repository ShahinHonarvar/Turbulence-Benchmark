
def find_original_set(*args):
    if len(args) != 84:
        raise ValueError('Exactly 84 sets are required')
    original_set = set()
    for argument in args:
        if not isinstance(argument, set):
            raise TypeError('All arguments must be sets')
        original_set.update(argument)
    return original_set
