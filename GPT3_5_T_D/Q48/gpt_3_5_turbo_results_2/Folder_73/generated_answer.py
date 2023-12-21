
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[76]
    result = 0
    for i in range(a + 1, b):
        if i not in nums[10:77]:
            result += i
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:]
