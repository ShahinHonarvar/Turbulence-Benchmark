
def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    sum = 0
    for i in range(a+1, b):
        if i not in nums[451:905]:
            sum += i
    if sum == 0:
        return ""
    else:
        if sum % 2 == 0:
            return hex(sum)[2:]
        else:
            return bin(sum)[2:]
