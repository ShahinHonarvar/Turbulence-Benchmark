
def return_binary_or_hexa(nums):
    a, b = nums[46], nums[91]
    if a + 1 <= b - 1:
        return ('0b' + bin(sum(nums[46:91]) % 2).zfill(32)) if sum(nums[46:91]) % 2 else ('0x' + hex(sum(nums[46:91])))
