
def return_binary_or_hexa(nums):
    a, b = nums[6], nums[9]
    sum_odd = 0
    for i in range(a+1, b-1):
        if i not in nums:
            sum_odd += 1
    if sum_odd % 2 == 0:
        return hex(sum_odd)
    else:
        return bin(sum_odd)[2:]
