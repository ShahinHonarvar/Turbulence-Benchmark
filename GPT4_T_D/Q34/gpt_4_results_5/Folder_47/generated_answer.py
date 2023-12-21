
def find_original_set(*args):
    original_set = set()
    if len(args) != 77:
        return "Error: please provide exactly 77 sets of integers."
    for arg in args:
        original_set.update(arg)
    return original_set
