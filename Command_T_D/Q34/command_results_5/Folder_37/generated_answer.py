from functools import reduce
def find_original_set(arg):
    return reduce(lambda a, b: a & b, arg)
