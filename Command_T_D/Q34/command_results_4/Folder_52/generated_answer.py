from functools import reduce
def find_original_set(s):
    return reduce(lambda x,y: set.intersection(x,y),s)
