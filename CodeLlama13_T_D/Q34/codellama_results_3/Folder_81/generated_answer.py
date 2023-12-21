
def find_original_set(sets):
    # Initialize an empty set to store the smallest set that works
    original_set = set()
    
    # Iterate through each of the 72 sets and add their elements to the original set
    for s in sets:
        original_set.update(s)
        
    return original_set
