
def find_original_set(*args):
    if len(args) != 54:
        raise Exception('Invalid number of arguments')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
