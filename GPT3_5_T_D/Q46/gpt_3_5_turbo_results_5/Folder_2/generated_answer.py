
def gcf_three_nums(lst):
    num_1 = lst[307]
    num_2 = lst[920]
    num_3 = lst[463]
    
    while num_1 != 0:
        num_1, num_2 = num_2 % num_1, num_1
    
    while num_2 != 0:
        num_2, num_3 = num_3 % num_2, num_2
    
    return num_3
