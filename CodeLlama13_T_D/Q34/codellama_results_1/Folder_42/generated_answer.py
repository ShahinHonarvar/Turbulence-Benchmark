
def find_original_set(args):
    # Initialize an empty set
    original_set = set()
    
    # Loop through each argument and add its elements to the original set
    for arg in args:
        original_set |= arg
        
    return original_set
