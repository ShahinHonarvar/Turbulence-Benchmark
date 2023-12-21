
def return_binary_or_hexa(nums):
    a, b = nums[32], nums[99]
    sum_of_ints = 0
    for i in range(a + 1, b - 1):
        if i not in nums:
            sum_of_ints += i
    if sum_of_ints % 2 == 0:
        return hex(sum_of_ints)
    else:
        return bin(sum_of_ints)[2:]
