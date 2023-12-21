
def return_binary_or_hexa(tuple_of_nums):
    a = tuple_of_nums[13]
    b = tuple_of_nums[76]
    missing_nums = {i for i in range(a + 1, b)} - set(tuple_of_nums[13:77])
    sum_of_missing_nums = sum(missing_nums)
    
    if sum_of_missing_nums == 0:
        return ""
    
    elif sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    
    else:
        return hex(sum_of_missing_nums)[2:].upper()
