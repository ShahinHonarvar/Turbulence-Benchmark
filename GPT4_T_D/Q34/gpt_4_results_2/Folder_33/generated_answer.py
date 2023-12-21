
def find_original_set(*args):
    if len(args) != 263:
        return "Error, number of arguments isn't 263."
    else:
        original_set = set()
        for arg in args:
            original_set = original_set.union(arg)
        return original_set
