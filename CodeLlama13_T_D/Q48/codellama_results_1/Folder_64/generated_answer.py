
def return_binary_or_hexa(nums):
    a, b = nums[0], nums[5]
    sum = 0
    for i in range(a+1, b):
        if i not in nums:
            sum += 1
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
