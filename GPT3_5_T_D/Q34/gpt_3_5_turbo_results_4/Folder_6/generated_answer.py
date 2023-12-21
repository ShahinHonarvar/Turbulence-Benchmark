
def find_original_set(*args):
    original_set = set()
    
    for set_arg in args:
        original_set.update(set_arg)
    
    return original_set
