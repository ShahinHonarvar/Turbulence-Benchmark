

def all_ints_div_by_num(lst):
    divisible_lst = []
    for i in range(417, 891):
        if lst[i] % -173 == 0:
            divisible_lst.append(lst[i])
    return divisible_lst
