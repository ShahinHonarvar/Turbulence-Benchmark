
def return_binary_or_hexa(nums):
    a, b = nums[1], nums[8]
    sum_int = sum(set(range(a+1, b)) - set(nums[1:9]))
    if sum_int == 0: 
        return ""
    else:     
        if sum_int % 2 == 1:
            return bin(sum_int)[2:]
        else: 
            return hex(sum_int)[2:].upper()
