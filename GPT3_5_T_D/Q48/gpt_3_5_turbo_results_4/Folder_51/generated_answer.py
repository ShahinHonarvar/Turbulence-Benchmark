
def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[9]
    sum = 0

    for i in range(a + 1, b):
        if i not in nums[6:9]:
            sum += i

    if sum == 0 or sum % 2 == 0:
        return hex(sum)[2:]
    
    return bin(sum)[2:]
