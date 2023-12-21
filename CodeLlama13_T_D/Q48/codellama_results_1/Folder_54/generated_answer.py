
def return_binary_or_hexa(nums):
    a, b = nums[35], nums[64]
    s = sum([i for i in range(a + 1, b) if i not in nums])
    if s % 2 == 0:
        return "{:x}".format(s)
    else:
        return bin(s)[2:]
