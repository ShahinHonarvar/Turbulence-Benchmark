
def return_binary_or_hexa(nums):
    a, b = sorted(set(nums) - set(nums[81:86]))
    if a > b:
        a, b = b, a
    return ("0b" + bin(a + 1 + sum(n for n in range(a + 1, b - 1) if n not in nums[81:86])).zfill(32)) if a + 1 + sum(range(a + 1, b - 1)) % 2 else hex(a + 1 + sum(range(a + 1, b - 1)))[2:])
