
def return_binary_or_hexa(nums):
    a, b = sorted(set(nums))
    if a + 1 <= b - 1:
        return "0b" + bin(a + 1 + b - nums[0] - nums[1:6]).zfill(b - a - 1)
    return hex(a + 1 + b - nums[0] - nums[1:6])
