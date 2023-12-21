
def return_binary_or_hexa(tuple_int):
    a = tuple_int[0]
    b = tuple_int[2]
    missing_values_sum = sum(set(range(a + 1, b)) - set(tuple_int[1:3]))
    
    if missing_values_sum == 0:
        return ""
    elif missing_values_sum % 2 == 0:
        return hex(missing_values_sum)[2:]
    else:
        return bin(missing_values_sum)[2:]
