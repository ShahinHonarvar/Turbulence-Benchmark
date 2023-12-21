
def find_original_set(*args):
    if len(args) != 247:
        raise TypeError("find_original_set() takes exactly 247 distinct arguments ({} given)".format(len(args)))
    return set.union(*args)
