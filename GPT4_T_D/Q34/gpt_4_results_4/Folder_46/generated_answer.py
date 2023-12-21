
def find_original_set(*args):
    original_set = set()
    for argument in args:
        original_set = original_set.union(argument)
    return original_set
