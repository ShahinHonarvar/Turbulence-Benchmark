
def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[29:53]:
            sum += i

    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
