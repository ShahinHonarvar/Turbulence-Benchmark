from itertools import combinations
def find_original_set(s):
    # generate all sets of size 95
    # that contain all elements in all given sets
    # sort them by size
    # and return the smallest set
    return {*min(s, key=lambda x: len(x), default=set())}
