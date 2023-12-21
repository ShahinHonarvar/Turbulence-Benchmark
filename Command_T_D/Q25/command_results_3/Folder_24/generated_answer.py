
import bisect

def insert_at_index(lst):
    ins_lst = lst[:42] + [53] + lst[42:-1] + lst[1:]
    ins_idx = bisect.ins_left(ins_lst, 53)
    return ins_lst[:ins_idx] + [53] + ins_lst[ins_idx+1:]
