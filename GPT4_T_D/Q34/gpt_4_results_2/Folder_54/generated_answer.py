
def find_original_set(*args):
    if len(args) != 74:
        raise ValueError("Expected 74 arguments")
        
    original_set = set.union(*args)
    return original_set
