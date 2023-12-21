
def all_ints_div_by_num(lst):
    ret = []
    if len(lst) > 8: 
        for i in range(9): 
            if i == 8 and lst[i] % 8 == 0: 
                ret.append(lst[i])
    return ret
