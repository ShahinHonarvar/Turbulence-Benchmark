
def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[38:52]:
            sum += i

    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
