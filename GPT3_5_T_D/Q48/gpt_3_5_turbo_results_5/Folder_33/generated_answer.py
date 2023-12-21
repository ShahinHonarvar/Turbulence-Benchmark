
def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    missing_nums = []
    for i in range(a + 1, b):
        if i not in nums[13:35]:
            missing_nums.append(i)
    if len(missing_nums) == 0:
        return ""
    else:
        sum_nums = sum(missing_nums)
        if sum_nums % 2 == 1:
            return format(sum_nums, 'b')
        else:
            return format(sum_nums, 'x')
