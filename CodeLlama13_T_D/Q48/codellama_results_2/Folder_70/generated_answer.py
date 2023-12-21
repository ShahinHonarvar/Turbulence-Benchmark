
def return_binary_or_hexa(nums):
    a, b = nums[43], nums[70]
    sum = 0
    for i in range(a + 1, b - 1 + 1):
        if not (i in nums and i >= 43 and i <= 70):
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper()[2:]
