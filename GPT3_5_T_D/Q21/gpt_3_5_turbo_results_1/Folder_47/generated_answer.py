
def all_ints_div_by_num(lst):
    res = []
    
    for num in lst[75:89]:
        if num % -27 == 0:
            res.append(num)
    
    return res
