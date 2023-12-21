
def return_binary_or_hexa(nums):
    a, b = nums[2], nums[7]
    s = sum(x for x in range(a + 1, b) if x not in nums[2:8])
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
