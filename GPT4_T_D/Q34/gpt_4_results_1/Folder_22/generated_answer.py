
def find_original_set(*args):
    if len(args) != 24:
        raise ValueError("Exactly 24 arguments are required")
    
    original_set = set()
    for arg_set in args:
        original_set = original_set.union(arg_set)
    
    return original_set
