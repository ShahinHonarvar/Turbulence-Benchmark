
def find_original_set(*args):
    if len(args) != 312:
        return "Error: The function should take exactly 312 arguments."
    else:
        original_set = set()
        for arg in args:
            original_set = original_set.union(arg)
        return original_set
