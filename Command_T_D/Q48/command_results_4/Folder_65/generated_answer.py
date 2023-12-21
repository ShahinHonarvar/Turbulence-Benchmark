
def return_binary_or_hexa(nums):
    a, b = nums[51], nums[76]
    val = sum(nums[i] for i in range(a + 1, b))
    return f"{val:b}" if val % 2 else f"{val:x}"
