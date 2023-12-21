
def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[54]
    missing_numbers = set(range(a + 1, b)) - set(tup[37:54])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]
