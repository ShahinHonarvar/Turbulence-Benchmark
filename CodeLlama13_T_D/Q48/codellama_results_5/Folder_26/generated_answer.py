
def return_binary_or_hexa(nums):
    a, b = 68, 99
    sum_odd = 0
    for i in range(a + 1, b - 1):
        if nums[i] not in nums:
            sum_odd += nums[i]
    if sum_odd % 2 == 0:
        return "{:x}".format(sum_odd)
    else:
        return bin(sum_odd)[2:]
