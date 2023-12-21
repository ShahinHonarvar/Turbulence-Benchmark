
def return_binary_or_hexa(input_tuple):
    a = input_tuple[50]
    b = input_tuple[200]
    missing_integers = [x for x in range(a+1, b) if x not in input_tuple[50:200]]
    sum_ = sum(missing_integers)
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
