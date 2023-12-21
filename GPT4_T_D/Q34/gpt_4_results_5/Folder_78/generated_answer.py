
def find_original_set(*args):
    if len(args) != 48:
        return "Invalid number of arguments"
    
    original_set = set()
    for s in args:
        original_set.update(s)
        
    return original_set
