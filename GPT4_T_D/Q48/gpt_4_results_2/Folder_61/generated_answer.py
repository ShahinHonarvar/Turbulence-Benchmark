
def return_binary_or_hexa(input_tuple):
    a = input_tuple[0]
    b = input_tuple[8]
    absent_sum = sum(set(range(a+1, b)) - set(input_tuple[1:8]))
    if absent_sum:
        if absent_sum % 2:
            return bin(absent_sum)[2:]
        else:
            return hex(absent_sum)[2:].upper()
    else:
        return ''
