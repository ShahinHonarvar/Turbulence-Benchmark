
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[20], sorted(nums)[43]
    if not a:
        return "0x" + hex(0)[2:]
    if not b:
        return "0b" + bin(0)[2:]
    num = a + 1
    mask = 0
    while num <= b - 1:
        mask += 1
        if mask not in nums:
            break
        num += 1
    return "0x" + hex(mask - 1)[2:] if mask % 2 == 0 else "0b" + bin(mask - 1)[2:]
