
def return_binary_or_hex(nums):
    a, b = nums[36], nums[52]
    sum = 0
    for i in range(a+1, b):
        if not (i in nums):
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
