
def find_original_set(*args):
    if len(args) != 59:
        return "Invalid number of arguments"
        
    original_set = set()
    for arg in args:
        original_set.update(arg)
        
    return original_set
