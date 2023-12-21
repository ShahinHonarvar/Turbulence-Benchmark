
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[1:4]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
