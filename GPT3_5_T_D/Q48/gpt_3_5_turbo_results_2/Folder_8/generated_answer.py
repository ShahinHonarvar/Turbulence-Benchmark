
def return_binary_or_hexa(nums):
    a = nums[45]
    b = nums[48]
    start = a + 1
    end = b - 1

    if start > end:
        return ""
    
    total = 0
    for num in range(start, end + 1):
        if num not in nums[46:48]:
            total += num
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
