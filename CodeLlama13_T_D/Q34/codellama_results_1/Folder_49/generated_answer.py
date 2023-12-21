
def find_original_set(args):
    # create an empty set to store the result
    original_set = set()
    
    # iterate over each argument and add its elements to the result set
    for arg in args:
        original_set |= arg
        
    return original_set
