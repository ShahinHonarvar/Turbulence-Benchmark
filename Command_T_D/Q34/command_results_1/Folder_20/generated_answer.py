from functools import reduce
def find_original_set(s):
    return reduce(lambda x, y: x & y, (set(range(len(s))), s))
