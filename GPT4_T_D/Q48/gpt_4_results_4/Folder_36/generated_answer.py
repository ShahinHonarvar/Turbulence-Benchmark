
def return_binary_or_hexa(nums):
    missing_nums = set(range(nums[110] + 1, nums[348])) - set(nums[110:349])
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ""
    elif num_sum % 2 == 1:
        return bin(num_sum)[2:]
    else:
        return hex(num_sum)[2:]
