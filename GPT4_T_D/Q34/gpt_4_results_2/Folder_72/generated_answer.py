
def find_original_set(*args):
    if len(args) != 87:
        raise ValueError("The function expects exactly 87 arguments.")
    
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("Each argument must be a set of integers.")
        original_set = original_set.union(arg)
    return original_set
