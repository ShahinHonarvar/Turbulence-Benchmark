
def return_binary_or_hexa(nums):
    a, b = nums[48], nums[76]
    r = sum(nums[a + 1:b] for n in range(a + 1, b) if n not in nums)
    return str(r) if r % 2 else hex(r)[2:]
