
def find_original_set(*args):
    if len(args) != 733:
        raise ValueError('Must provide 733 distinct arguments')
    
    original_set = set()
    for arg in args:
        original_set.update(arg)
    
    return original_set
