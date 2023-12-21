
def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('You must provide exactly 321 sets.')
    original_set = set()
    for curr_set in args:
        original_set.update(curr_set)
    return original_set
