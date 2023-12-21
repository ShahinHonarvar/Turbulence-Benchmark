
def return_binary_or_hexa(tuple):
    a, b = tuple[49], tuple[74]
    nums_not_in_tuple = set(range(a + 1, b)) - set(tuple[49:75])
    sum_nums = sum(nums_not_in_tuple)
    if sum_nums == 0: 
        return ''
    elif sum_nums % 2 == 0: 
        return hex(sum_nums)[2:]
    else: 
        return bin(sum_nums)[2:]
