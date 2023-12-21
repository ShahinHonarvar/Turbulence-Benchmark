
def gcf_three_nums(lst):
    num_1 = lst[78]
    num_2 = lst[19]
    num_3 = lst[13]
    
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    
    while num_1 != 0:
        num_3, num_1 = num_1, num_3 % num_1
    
    return num_3
