
def return_binary_or_hexa(input_tuple):
    a = input_tuple[38]
    b = input_tuple[81]
    gap_integers = set(range(a + 1, b))
    available_integers = set(input_tuple[38:81])
    missing_integers = gap_integers - available_integers
    total_sum = sum(missing_integers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum != 0:
        return hex(total_sum)[2:].upper()
    else:
        return ""
