
def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    total = sum([i for i in range(a+1, b) if i not in nums[60:91]])
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
