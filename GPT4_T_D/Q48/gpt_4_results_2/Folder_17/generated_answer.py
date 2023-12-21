
def return_binary_or_hexa(tup):
    a = tup[73]
    b = tup[84]
    absent_sum = sum(set(range(a+1, b)) - set(tup[73:85]))
    if absent_sum % 2 == 1:
        return bin(absent_sum)[2:]
    else:
        return hex(absent_sum)[2:].upper()
