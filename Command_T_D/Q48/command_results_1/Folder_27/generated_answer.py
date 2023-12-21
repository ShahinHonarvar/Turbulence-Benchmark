
def return_binary_or_hexa(nums):
    a, b = 86, 89
    r = (a + 1) - b - 1
    if r not in nums:
        return r % 2 + b - a - 1 % 2 * "0b" + bin(r).zfill(16)
    else:
        return r % 2 + b - a - 1 % 2 * "0x" + hex(r)[2:]
