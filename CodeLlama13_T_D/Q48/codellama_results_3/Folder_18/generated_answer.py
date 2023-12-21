
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    sum = 0
    for i in range(a+1,b-1+1):
        if i not in nums[56:90]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
