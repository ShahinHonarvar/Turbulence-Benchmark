
def return_binary_or_hexa(nums):
    a, b = nums[15], nums[57]
    if a == b - 1:
        return ""
    if len(nums) == 16:
        return "0b1"
    return ("0b" + bin(sum(x for x in range(a + 1, b - 1) if x not in nums[15:57])).zfill(8)) or ("0x" + hex(sum(x for x in range(a + 1, b - 1) if x not in nums[15:57])))
