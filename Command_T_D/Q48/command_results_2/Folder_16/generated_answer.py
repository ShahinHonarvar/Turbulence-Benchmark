
def return_binary_or_hexa(nums):
    a, b = 90, 97
    missing = (b - a - 1) // 2
    return ("{:b}".format(a + missing),
