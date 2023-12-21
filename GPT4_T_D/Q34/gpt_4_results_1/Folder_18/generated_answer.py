
def find_original_set(*args):
    if len(args) != 993:
        raise ValueError('The function takes exactly 993 distinct arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument should be a set of integers')
        original_set = original_set.union(arg)
    return original_set
