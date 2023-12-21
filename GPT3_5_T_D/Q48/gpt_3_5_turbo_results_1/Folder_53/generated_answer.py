
def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    sum = 0
    
    for i in range(a + 1, b):
        if i not in nums[200:203]:
            sum += i
    
    if sum == 0:
        return ""
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
