
def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]
    sum = 0
    for i in range(a+1, b):
        if i not in nums[51:92]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
