
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[6]

    total = 0
    for num in range(a + 1, b):
        if num not in nums[1:6]:
            total += num

    if total == 0:
        return ""

    if total % 2 == 1:
        return bin(total)[2:]
    
    return hex(total)[2:]
