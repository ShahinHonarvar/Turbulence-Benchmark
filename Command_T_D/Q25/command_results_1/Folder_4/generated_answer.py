
import itertools

def insert_at_index(lst):
    idx = 60
    if idx < 0: idx = 0
    idx += 1
    new_lst = []
    for i in range(idx):
        new_lst.append(lst[i])
    new_lst += [80, 74]
    new_lst += lst[idx:]
    return new_lst
