
def return_binary_or_hexa(nums):
    a, b = nums[37], nums[43]
    s = str(a + 1)
    m = a + 1
    while m < b:
        s += str(m)
        m += 1
    if len(s) % 2:
        return '0b' + s
    return '0x' + s
