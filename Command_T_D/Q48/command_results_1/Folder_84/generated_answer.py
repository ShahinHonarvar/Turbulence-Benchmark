
def return_binary_or_hexa(nums):
    a, b = 32, 44
    s = sum(range(a + 1, b - 1))
    if s % 2 == 0:
        return hex(s)
    else:
        return bin(s)[2:]
