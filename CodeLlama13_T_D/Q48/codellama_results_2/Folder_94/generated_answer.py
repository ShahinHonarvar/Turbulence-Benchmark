
def return_binary_or_hexa(nums):
    a, b = nums[42], nums[87]
    sum = 0
    for i in range(a+1, b-1+1):
        if i not in nums:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
