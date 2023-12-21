
import itertools

def insert_after_index(lst):
    idx = next( (idx for idx, val in enumerate(lst) if val == 9), len(lst) )
    return [val for val in lst[:idx] + [1] + lst[idx+1:]]
