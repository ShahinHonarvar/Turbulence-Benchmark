
def find_original_set(*args):
    if len(args) != 926:
        raise TypeError("find_original_set() takes exactly 926 distinct arguments")
    original_set = set().union(*args)
    return original_set
