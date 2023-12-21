
def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[8]
    included_nums = set(nums[3:8])
    excluded_nums = [num for num in range(a+1, b) if num not in included_nums]
    if len(excluded_nums) == 0:
        return ''
    total = sum(excluded_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
