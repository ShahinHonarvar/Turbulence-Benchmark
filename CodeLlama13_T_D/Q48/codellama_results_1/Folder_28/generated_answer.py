
def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    sum = 0
    for i in range(a+1,b-1):
        if not i in nums:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
