
def find_original_set(*args):
    # Initialize an empty set to store the final result
    original_set = set()
    
    # Iterate over all given arguments (sets of integers)
    for arg in args:
        # Add all elements from current argument to the final set
        original_set |= arg
        
    return original_set
