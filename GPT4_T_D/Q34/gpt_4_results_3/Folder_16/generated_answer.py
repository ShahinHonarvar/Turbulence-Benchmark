
def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('The function arguments are not as per specification.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('The function arguments are not as per specification.')
        original_set = original_set.union(arg)
    return original_set
