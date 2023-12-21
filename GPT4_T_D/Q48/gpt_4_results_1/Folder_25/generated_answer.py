
def return_binary_or_hexa(tuple_input):
    a = tuple_input[37]
    b = tuple_input[43]
    to_exclude = tuple_input[38:43]
    sum_ = sum(set(range(a + 1, b)) - set(to_exclude))
    if sum_ == 0:
        return ''
    elif sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
