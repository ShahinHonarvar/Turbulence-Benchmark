
def find_original_set(*args):
    # Check if all args are sets of integers
    if not all(isinstance(arg, set) and arg and all(isinstance(x, int) for x in arg) for arg in args):
        raise ValueError("All arguments must be non-empty sets of integers")
    
    # Find the smallest set that contains all elements from all given sets
    original_set = set()
    for arg in args:
        original_set |= arg
    
    return original_set
