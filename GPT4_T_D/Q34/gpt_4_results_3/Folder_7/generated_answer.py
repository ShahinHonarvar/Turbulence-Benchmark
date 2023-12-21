
def find_original_set(*args):
    if len(args) != 537:
        raise ValueError("A total of 537 sets are required")
    return_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments must be sets")
        return_set = return_set.union(arg)
    return return_set
