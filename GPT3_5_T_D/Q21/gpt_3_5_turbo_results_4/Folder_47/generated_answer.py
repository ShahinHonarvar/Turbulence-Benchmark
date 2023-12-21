
def all_ints_div_by_num(lst):
    divisible_list = []
    
    for i in range(75, 89):
        if i < len(lst) and lst[i] % -27 == 0:
            divisible_list.append(lst[i])
    
    return divisible_list
