
def return_binary_or_hexa(integers):
    a = integers[46]
    b = integers[91]
    sum_ = sum(set(range(a + 1, b)) - set(integers[46:92]))

    if sum_ == 0:
        return ''
    elif sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
