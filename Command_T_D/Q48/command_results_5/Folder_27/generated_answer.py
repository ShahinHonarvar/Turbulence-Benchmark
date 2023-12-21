
def return_binary_or_hexa(nums):
    a, b = sorted(set(nums) - set((nums[86], nums[89])))
    if not a:
        return ""
    if b == a + 1:
        return "0b" + str(2**32 + a)
    return "0b" + str(2**32 + a) if 2**32 + a % 2 == 1 else "0x" + hex(2**32 + a)
