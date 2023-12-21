
def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[60:91]]
    if missing_nums:
        sum_of_missing = sum(missing_nums)
        if sum_of_missing % 2 == 1:
            return bin(sum_of_missing)[2:]
        else:
            return hex(sum_of_missing)[2:]
    else:
        return ""
