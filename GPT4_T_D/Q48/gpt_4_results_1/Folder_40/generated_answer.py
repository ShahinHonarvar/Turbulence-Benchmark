
def return_binary_or_hexa(int_tuple):
    a = int_tuple[0]
    b = int_tuple[3]
    missing_nums = [i for i in range(a + 1, b) if i not in int_tuple]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
