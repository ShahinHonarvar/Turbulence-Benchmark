
def find_original_set(*args):
    original_set = set(args[0])  # create the initial set using the first argument
    for arg in args[1:]:  # iterate over the remaining arguments
        original_set |= set(arg)  # union the current argument with the existing set
    return original_set
