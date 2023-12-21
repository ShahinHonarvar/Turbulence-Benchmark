from functools import reduce
def find_original_set(arg_set):
    return reduce(lambda x,y:x&y, arg_set)
