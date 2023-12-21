
def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    sum_ab = sum(set(range(a + 1, b)) - set(numbers[81:87]))
    if sum_ab % 2 == 0:
        return hex(sum_ab).lstrip("0x").upper()
    else:
        return bin(sum_ab).lstrip("0b")
