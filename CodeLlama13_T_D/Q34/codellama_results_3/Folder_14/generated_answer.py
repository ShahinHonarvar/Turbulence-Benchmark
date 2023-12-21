
def find_original_set(*args):
    # Flatten the arguments into a single list of integers
    all_integers = [i for sublist in args for i in sublist]
    
    # Create a set from the flattened list
    original_set = set(all_integers)
    
    return original_set
