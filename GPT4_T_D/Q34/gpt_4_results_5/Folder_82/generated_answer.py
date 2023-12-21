
def find_original_set(*args):
    if len(args) != 47:
        return "Error: 47 sets of integers are required"
    
    original_set = set()
    
    for arg in args:
        original_set = original_set.union(arg)
        
    return original_set
