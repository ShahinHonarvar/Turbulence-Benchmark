
def return_binary_or_hexa(tup):
    a, b = tup[36], tup[52]
    nums = set(range(a + 1, b))
    missing_nums = nums.difference(tup[37:52])
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
        
    return ''
