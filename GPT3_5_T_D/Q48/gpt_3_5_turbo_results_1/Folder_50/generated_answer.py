
def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[76]
    s = 0
    for i in range(a + 1, b):
        if i not in nums[13:76]:
            s += i
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
