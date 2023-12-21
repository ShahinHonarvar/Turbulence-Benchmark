
def find_original_set(*args):
    if len(args) != 85:
        raise Exception("Should have exactly 85 distinct arguments.")
        
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
