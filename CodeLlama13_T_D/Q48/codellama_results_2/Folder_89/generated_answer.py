
def return_binary_or_hexa(nums):
    a, b = nums[54], nums[83]
    s = sum(i for i in range(a + 1, b) if i not in nums)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
