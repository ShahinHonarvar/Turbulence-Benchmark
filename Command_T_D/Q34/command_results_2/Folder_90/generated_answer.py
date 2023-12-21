from functools import reduce
def find_original_set(s):
    return reduce(lambda a,b:a|b,s)
