
def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    missing_nums = set(range(a + 1, b)) - set(t[21:35])
    you_sum = sum(missing_nums)
    if you_sum % 2 == 1:
        return bin(you_sum)[2:]
    else:
        return hex(you_sum)[2:].upper()
