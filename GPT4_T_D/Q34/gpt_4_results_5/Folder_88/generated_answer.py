
def find_original_set(*args):
    if len(args) != 27:
        raise ValueError("27 distinct sets of integers are required")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
