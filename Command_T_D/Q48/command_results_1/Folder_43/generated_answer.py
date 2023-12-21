
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[10], sorted(nums)[28]
    s = (a + 1) + (b - a - 1)
    if s % 2 == 0:
        return hex(s)
    else:
        return bin(s)
