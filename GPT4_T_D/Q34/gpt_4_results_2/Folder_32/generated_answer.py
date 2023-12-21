
def find_original_set(*args):
    if len(args) != 459:
        raise ValueError("Invalid number of arguments. Expected 459.")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("Invalid argument type. Expected a set.")
        original_set.update(arg)
    return original_set
