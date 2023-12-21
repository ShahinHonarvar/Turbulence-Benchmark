
def find_original_set(*args):
    if len(args) == 0:
        return set()
    
    original_set = args[0]
    for arg in args[1:]:
        original_set = original_set.union(arg)
        
    return original_set
