
def return_binary_or_hexa(tup):
    a, b = tup[36], tup[85]
    required_nums = set(range(a+1, b))
    present_nums = set(tup[36:86])
    missing_nums = required_nums - present_nums
    sum_missing = sum(missing_nums)
    
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    elif sum_missing % 2 == 0 and sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ""
