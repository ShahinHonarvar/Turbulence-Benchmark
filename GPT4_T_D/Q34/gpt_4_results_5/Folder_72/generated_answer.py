
def find_original_set(*args):
    if len(args) != 87:
        raise ValueError("The function expected 87 arguments but got {}".format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments should be of type 'set'")
        original_set.update(arg)
    return original_set
