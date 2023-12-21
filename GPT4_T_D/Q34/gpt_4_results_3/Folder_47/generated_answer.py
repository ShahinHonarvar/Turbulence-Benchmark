
def find_original_set(*args):
    if len(args) != 77:
        return "This function requires exactly 77 distinct arguments."
    else:
        original_set = set()
        for arg in args:
            original_set = original_set.union(arg)
        return original_set
