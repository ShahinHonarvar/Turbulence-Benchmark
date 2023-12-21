
def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[67]
    missing_nums = []
    for num in range(a+1, b):
        if num not in nums[44:67]:
            missing_nums.append(num)
    if len(missing_nums) == 0:
        return ""
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
