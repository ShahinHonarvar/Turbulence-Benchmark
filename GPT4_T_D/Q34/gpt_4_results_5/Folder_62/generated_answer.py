
def find_original_set(*args):
    if len(args) != 790:
        raise Exception('Invalid number of arguments provided')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
