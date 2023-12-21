
def find_original_set(sets):
    # Initialize an empty set to store the result
    original_set = set()
    
    # Iterate through each set in sets
    for s in sets:
        # Add all elements in current set to the result set
        original_set |= s
        
    return original_set
