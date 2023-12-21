
def return_binary_or_hexa(nums):
    a, b = nums[70], nums[98]
    sum = 0
    for i in range(a + 1, b - 1 + 1):
        if i not in nums:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper()[2:]
