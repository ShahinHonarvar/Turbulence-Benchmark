
def return_binary_or_hexa(nums):
    a, b = nums[11], nums[76]
    result = 0
    for i in range(a+1, b):
        if i not in nums:
            result += i
    return str(bin(result)[2:]) if result % 2 else str(hex(result))[2:]
