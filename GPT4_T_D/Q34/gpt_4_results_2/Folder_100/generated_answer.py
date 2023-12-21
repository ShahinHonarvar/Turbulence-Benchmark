
def find_original_set(*args):
    if len(args) != 91:
        raise ValueError("Number of arguments should be exactly 91")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
