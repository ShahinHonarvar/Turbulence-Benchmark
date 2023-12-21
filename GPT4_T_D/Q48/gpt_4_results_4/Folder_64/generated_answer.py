
def return_binary_or_hexa(nums):
    a, b = nums[0], nums[5]
    sum_val = sum(set(range(a+1, b)) - set(nums[:6]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
