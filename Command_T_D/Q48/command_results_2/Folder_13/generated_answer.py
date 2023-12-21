
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[46], sorted(nums)[91]
    if a == b:
        return ""
    odd = sum(nums[a:b]) % 2
    if odd:
        return bin(sum(nums[a + 1:b - 1])).zfill(64)
    else:
        return hex(sum(nums[a + 1:b - 1])).zfill(32)
