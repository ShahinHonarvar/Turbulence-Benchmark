
def return_binary_or_hexa(nums):
    a = nums[44] + 1
    b = nums[78] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in nums:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
