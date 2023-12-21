
def return_binary_or_hexa(input_tuple):
    a = input_tuple[36]
    b = input_tuple[85]

    total = sum(set(range(a+1, b)) - set(input_tuple[36:86]))

    if total == 0:
        return ""
    elif total%2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
