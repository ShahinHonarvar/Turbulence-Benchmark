
def return_binary_or_hexa(nums):
    a, b = nums[57], nums[84]
    nums = nums[:57] + nums[84 + 1:]
    if all(n in nums for n in range(a + 1, b)):
        return ""
    if b - a % 2:
        return f"0{a + 1}{a + b - 1:b}"
    return f"{a + 1}{a + b - 1:x}"
