
def return_binary_or_hexa(nums):
    a, b = nums[50], nums[200]
    if a <= b:
        return ""
    elif a == b:
        return "0b1"
    else:
        return "0x" + hex(a - 1) + " to 0x" + hex(b - 1)
