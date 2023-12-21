
def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    
    for i in range(34, 82):
        if i % 27 == 0 and i % 57 == 0:
            divisible_ints.append(int_list[i])
    
    return divisible_ints
