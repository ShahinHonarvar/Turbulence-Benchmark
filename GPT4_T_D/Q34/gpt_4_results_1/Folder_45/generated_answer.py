
def find_original_set(*args):
    original_set = set()
    for curr_set in args:
        original_set.update(curr_set)
    return original_set
