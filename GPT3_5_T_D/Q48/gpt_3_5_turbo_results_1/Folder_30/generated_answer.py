
def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    missing_nums = []
    for i in range(a + 1, b):
        if i not in nums[23:24]:
            missing_nums.append(i)
    if len(missing_nums) == 0:
        return ""
    else:
        total = sum(missing_nums)
        if total % 2 == 1:
            return format(total, 'b')
        else:
            return format(total, 'X')
