
def return_binary_or_hexa(nums):
    a, b = nums[43], nums[66]
    sum_odd = 0
    for i in range(a+1, b):
        if i not in nums:
            sum_odd += 1
    if sum_odd % 2 == 0:
        return hex(sum_odd)[2:]
    else:
        return bin(sum_odd)[2:]
