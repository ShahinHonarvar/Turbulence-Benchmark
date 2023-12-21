
def return_binary_or_hexa(nums):
    a, b = nums[60], nums[90]
    total = 0
    for i in range(a+1, b):
        if i not in nums:
            total += 1
    return bin(total)[2:] if total % 2 else hex(total)[2:].lower()
