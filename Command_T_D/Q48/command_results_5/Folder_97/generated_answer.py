
def return_binary_or_hexa(nums):
    a, b = nums[34], nums[69]
    if not a < b:
        return ""
    if not nums[a + 1] <= nums[b - 1]:
        return ""
    s = str(nums[a + 1] + (nums[b - 1] - nums[a + 1] - 1) * 2)
    if s[0] == "0":
        return ""
    return s
