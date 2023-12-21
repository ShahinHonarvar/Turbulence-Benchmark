
def find_original_set(*args):
    original_set = set()
    
    for arg in args:
        original_set.update(arg)
    
    return original_set
