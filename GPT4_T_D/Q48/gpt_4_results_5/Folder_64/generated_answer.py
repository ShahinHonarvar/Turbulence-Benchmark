
def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[5]
    
    nums_in_tup = set(tup[1:5])
    missing_nums = [i for i in range(a+1, b) if i not in nums_in_tup]
    
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
