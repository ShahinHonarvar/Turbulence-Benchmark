
def return_binary_or_hexa(nums):
    a, b = nums[1], nums[4]
    sum = 0
    for i in range(a+1, b):
        if i not in nums:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
