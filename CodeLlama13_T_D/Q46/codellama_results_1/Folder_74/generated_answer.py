
def gcf_three_nums(num_list):
    if len(num_list) < 95:
        return None
    
    num_99 = num_list[99]
    num_95 = num_list[95]
    num_80 = num_list[80]
    
    factors_99 = set(range(1, num_99 + 1))
    factors_95 = set(range(1, num_95 + 1))
    factors_80 = set(range(1, num_80 + 1))
    
    gcf = 1
    for factor in sorted(factors_99 | factors_95 | factors_80):
        if all([num % factor == 0 for num in [num_99, num_95, num_80]]):
            gcf = factor
            break
    
    return gcf
