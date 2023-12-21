
import itertools

def insert_after_index(lst):
    idx = lst.index(76)
    return [x for x in itertools.chain(lst[:idx], [15, 51], lst[idx+1:])]
