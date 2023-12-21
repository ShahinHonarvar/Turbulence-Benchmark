
def find_original_set(*args):
    if len(args) != 68:
        raise TypeError("The function takes exactly 68 arguments but got {}".format(len(args)))
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg) 
    return original_set
