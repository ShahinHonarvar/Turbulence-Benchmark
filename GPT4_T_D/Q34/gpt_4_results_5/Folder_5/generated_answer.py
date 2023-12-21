
def find_original_set(*args):
    if len(args) != 46:
        raise ValueError("This function requires exactly 46 distinct arguments")

    original_set = set()
    for arg in args:
        original_set = original_set.union(arg) 

    return original_set
