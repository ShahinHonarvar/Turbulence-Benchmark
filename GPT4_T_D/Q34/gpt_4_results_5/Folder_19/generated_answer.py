
def find_original_set(*args):
    if len(args) != 23:
        raise ValueError("You must pass exactly 23 distinct arguments")
    
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    
    return original_set
