
def find_original_set(*args):
    if len(args) != 410:
        raise ValueError("The function expects 410 sets.")
        
    original_set = set().union(*args)
    return original_set
