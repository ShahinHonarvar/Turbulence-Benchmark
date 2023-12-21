
def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
