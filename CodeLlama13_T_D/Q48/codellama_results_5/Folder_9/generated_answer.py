
def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[200]
    sum = 0
    for i in range(a+1, b-1):
        if not i in nums:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
