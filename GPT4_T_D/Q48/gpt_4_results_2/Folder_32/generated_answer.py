
def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[90]
    excl_nums = set(tup[86:91])
    calc_nums = set(range(a+1, b))
    excl_nums = calc_nums.difference(excl_nums)
    excl_sum = sum(excl_nums)
    if excl_sum % 2 == 1: # if sum is odd
        return bin(excl_sum)[2:] # returns binary representation without '0b' prefix
    else: 
        return hex(excl_sum)[2:].upper() # returns hexadecimal representation without '0x' prefix
    return ""
