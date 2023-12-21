from functools import reduce
def find_original_set(s):
    s = reduce(lambda x,y:x|y,s)
    return s
