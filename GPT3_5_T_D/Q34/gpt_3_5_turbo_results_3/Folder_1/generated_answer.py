
def find_original_set(*args):
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set
