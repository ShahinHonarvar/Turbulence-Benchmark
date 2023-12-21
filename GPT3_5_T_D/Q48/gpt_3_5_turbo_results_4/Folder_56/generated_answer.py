
def return_binary_or_hexa(nums):
    a = nums[7]
    b = nums[9]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[7:9]]
    if len(missing_nums) == 0:
        return ""
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]
