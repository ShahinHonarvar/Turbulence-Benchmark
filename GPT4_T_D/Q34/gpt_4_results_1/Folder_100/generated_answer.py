
def find_original_set(*args):
    if len(args) != 91:
        raise ValueError("Expected 91 arguments")
    original_set = set()
    for arg in args:
        original_set.update(arg)
        
    return original_set
