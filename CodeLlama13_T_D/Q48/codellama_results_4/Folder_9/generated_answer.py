
def return_binary_or_hexa(nums):
    a = nums[70] + 1
    b = nums[200] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in nums:
            sum += 1
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
