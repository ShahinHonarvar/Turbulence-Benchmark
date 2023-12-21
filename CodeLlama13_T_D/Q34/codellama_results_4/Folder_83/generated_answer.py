
def find_original_set(args):
    # Initialize an empty set to store the final result
    original_set = set()
    
    # Iterate through each argument and update the original set accordingly
    for arg in args:
        original_set |= arg
        
    return original_set
