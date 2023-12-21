
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[200], sorted(nums)[202]
    if a == b - 1:
        return ""
    odd = 0
    for i in range(a + 1, b - 1):
        if i not in nums:
            odd += 1
    if odd % 2:
        return "0b" + bin(odd).zfill(8).decode("utf-8")
    else:
        return "0x" + hex(odd).zfill(4).decode("utf-8")
