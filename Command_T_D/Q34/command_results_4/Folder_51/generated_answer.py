from functools import reduce
def find_original_set(S):
    return reduce(lambda x,y:x|y,S)
