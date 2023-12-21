
def all_ints_div_by_both_two_nums(lst):
    start = 77
    end = 87
    divisible_by_23 = []
    divisible_by_57 = []
    
    for i in range(start, end+1):
        if lst[i] % 23 == 0:
            divisible_by_23.append(lst[i])
        if lst[i] % 57 == 0:
            divisible_by_57.append(lst[i])
    
    return [x for x in divisible_by_23 if x in divisible_by_57]
