
def return_binary_or_hexa(integers):
    a = integers[6]
    b = integers[9]
    absent_values = set(range(a + 1, b)) - set(integers[6:10])
    total = sum(absent_values)
    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
