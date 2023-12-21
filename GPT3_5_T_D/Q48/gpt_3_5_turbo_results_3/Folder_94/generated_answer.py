
def return_binary_or_hexa(nums):
    a = nums[42]
    b = nums[87]
    total = 0
    for num in range(a + 1, b):
        if num not in nums[42:87]:
            total += num
    
    if total == 0:
        return ""
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
