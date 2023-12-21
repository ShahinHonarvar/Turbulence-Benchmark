
def find_original_set(*args):
    if len(args) != 15:
        raise ValueError("Expected 15 sets of integers, got {}".format(len(args)))

    sets = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("Argument must be a set")
        sets.update(arg)

    return sets
