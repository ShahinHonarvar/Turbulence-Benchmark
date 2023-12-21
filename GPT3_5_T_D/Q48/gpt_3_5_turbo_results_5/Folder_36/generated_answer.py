
def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    sum = 0
    for num in range(a + 1, b):
        if num not in nums[110:349]:
            sum += num
    
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
