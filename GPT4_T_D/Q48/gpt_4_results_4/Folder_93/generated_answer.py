
def return_binary_or_hexa(nums):
    a, b = nums[57], nums[85]
    sum_numbers = sum(set(range(a+1, b)) - set(nums[57:86]))
    if sum_numbers == 0:
        return ""
    elif sum_numbers % 2 != 0:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:].upper()
