
def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[90]
    b = sorted_tuple[200]
    missing_sum = sum(set(range(a + 1, b)) - set(sorted_tuple[90:201]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
