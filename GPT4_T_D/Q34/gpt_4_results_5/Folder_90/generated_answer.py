
def find_original_set(*args):
    if len(args) != 985:
        raise ValueError("The function requires exactly 985 distinct arguments")
    original_set = set.union(*args)
    return original_set
