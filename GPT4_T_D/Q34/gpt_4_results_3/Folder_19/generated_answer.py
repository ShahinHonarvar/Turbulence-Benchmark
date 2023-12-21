
def find_original_set(*args):
    if len(args) != 23:
        raise Exception("Expected 23 arguments")
        
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    
    return original_set
