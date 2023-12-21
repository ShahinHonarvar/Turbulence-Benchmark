
def find_original_set(*args):
    if len(args) != 60:
        raise ValueError("The function expects exactly 60 arguments")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("Each argument should be a set")
        original_set.update(arg)
    return original_set
