
def return_binary_or_hexa(nums):
    a, b = nums[17], nums[88]
    sum_not_present = 0
    for i in range(a + 1, b - 1):
        if i not in nums:
            sum_not_present += i
    if sum_not_present % 2 == 0:
        return format(sum_not_present, "x")
    else:
        return bin(sum_not_present)[2:]
