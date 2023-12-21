
def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    difference = set(range(a+1, b)) - set(nums[69:99])
    diff_sum = sum(difference)
    if diff_sum == 0:
        return ""
    elif diff_sum % 2 == 0:
        return hex(diff_sum)[2:]
    else:
        return bin(diff_sum)[2:]
