
def return_binary_or_hexa(nums):
    a, b = 16, 87
    if a + 1 <= b - 1:
        return "0b{:b}".format(sum(range(a + 1, b - 1)))
    return "0x{:x}".format(sum(range(a + 1, b - 1)))
