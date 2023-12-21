
def find_original_set(*args):

    if len(args) != 40:
        raise ValueError("Exactly 40 sets are required")
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
        
    return original_set
