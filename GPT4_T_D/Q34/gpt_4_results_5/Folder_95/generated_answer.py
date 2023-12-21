
def find_original_set(*args):
    if len(args) != 88:
        raise ValueError("You need to provide exactly 88 distinct sets")
        
    original_set = set()
    for s in args:
        original_set.update(s)
        
    return original_set
