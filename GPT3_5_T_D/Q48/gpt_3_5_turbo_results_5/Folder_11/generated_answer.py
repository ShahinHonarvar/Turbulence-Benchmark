
def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    result = 0

    for num in range(a + 1, b):
        if num not in nums[48:76]:
            result += num

    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()
