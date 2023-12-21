
def return_binary_or_hexa(nums):
    a = nums[51]
    b = nums[76]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[51:77]]
    if len(missing_nums) == 0:
        return ""
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
