
def find_original_set(*sets):
    # Create an empty set to store the result
    original_set = set()
    
    # Iterate over each argument set
    for arg_set in sets:
        # Add each element of the argument set to the result set
        original_set.update(arg_set)
    
    return original_set
