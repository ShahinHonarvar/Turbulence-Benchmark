
def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[76]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in nums[13:77]:
            total_sum += i
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
