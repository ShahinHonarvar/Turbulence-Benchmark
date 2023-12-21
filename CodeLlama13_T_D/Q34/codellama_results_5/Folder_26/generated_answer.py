
def find_original_set(args):
    # Initialize an empty set
    original_set = set()
    
    # Iterate over the arguments
    for arg in args:
        # Add each element of the argument to the original set
        original_set |= arg
    
    return original_set
