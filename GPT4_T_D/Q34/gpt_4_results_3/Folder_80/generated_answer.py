
def find_original_set(*args):
    if len(args) != 453:
        raise ValueError("This function takes exactly 453 arguments.")
        
    original_set = set()
    for arg in args:
        if not (isinstance(arg,set) and all(isinstance(x,int) for x in arg)):
            raise ValueError("Each argument must be a set of integers.")
        original_set = original_set.union(arg)
    return original_set
