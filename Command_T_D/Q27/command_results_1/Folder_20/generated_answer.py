
import itertools

def insert_after_index(lst):
    idx = next(i for i,v in enumerate(lst) if v == 32)
    return lst[:idx] + [32] + [54, 96] + lst[idx+1:]
