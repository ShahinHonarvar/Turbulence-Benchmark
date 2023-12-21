
def return_binary_or_hexa(tuple_int):
    a = tuple_int[0]
    b = tuple_int[4]
    missing_integers_sum = sum(set(range(a + 1, b)) - set(tuple_int[0:5]))
    if missing_integers_sum % 2 == 1:
        return bin(missing_integers_sum)[2:]
    else:
        return hex(missing_integers_sum)[2:].upper()
