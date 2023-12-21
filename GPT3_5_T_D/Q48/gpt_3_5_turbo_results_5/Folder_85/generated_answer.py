
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    total = 0
    
    for i in range(a+1, b):
        if i not in nums[1:8]:
            total += i
    
    if total == 0:
        return ""
    elif total % 2 == 1:
        return str(bin(total)[2:])
    else:
        return str(hex(total)[2:])
