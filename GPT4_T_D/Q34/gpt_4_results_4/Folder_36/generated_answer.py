
def find_original_set(*args):
    if len(args) != 714:
        raise ValueError("Function takes exactly 714 arguments")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("Each argument must be a set of integers")
        original_set.update(arg)
    return original_set
