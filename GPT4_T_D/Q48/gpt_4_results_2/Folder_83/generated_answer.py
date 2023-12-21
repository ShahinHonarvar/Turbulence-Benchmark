
def return_binary_or_hexa(tup):
    a_index = 90
    b_index = 200
    a = tup[a_index]
    b = tup[b_index]
    present = set(tup[a_index+1:b_index])
    missing_sum = sum(set(range(a+1, b)) - present)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]  # Removing '0x' prefix
    else:
        return bin(missing_sum)[2:]  # Removing '0b' prefix
