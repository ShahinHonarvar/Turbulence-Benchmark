
def return_binary_or_hexa(nums):
    a = nums[80]
    b = nums[200]
    
    if b - a <= 1:
        return ""
    
    total = sum(nums[a+1:b])
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
