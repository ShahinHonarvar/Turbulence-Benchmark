
def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[52]
    sum = 0
    for i in range(a+1, b-1):
        if i not in nums:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
