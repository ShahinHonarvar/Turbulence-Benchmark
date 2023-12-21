
def return_binary_or_hexa(nums):
    a, b = nums[56], nums[88]
    s = sum([i for i in range(a+1, b) if i not in nums])
    return bin(s)[2:] if s % 2 else hex(s).upper()[2:]
