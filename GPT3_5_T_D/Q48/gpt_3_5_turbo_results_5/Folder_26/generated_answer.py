
def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[68:99]]
    if len(missing_nums) == 0:
        return ""
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]
