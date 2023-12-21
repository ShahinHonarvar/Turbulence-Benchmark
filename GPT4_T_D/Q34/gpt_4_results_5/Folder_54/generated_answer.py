
def find_original_set(*args):
    if len(args) != 74: 
        return "Error: Invalid number of arguments"
        
    original_set = set()
    for arg in args:
        if isinstance(arg, set):
            for item in arg:
                original_set.add(item)
        else:
            return "Error: All arguments must be sets of integers"
    return original_set
