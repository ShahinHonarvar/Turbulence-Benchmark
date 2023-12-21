
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[42]
    b = tuple_of_integers[87]
    indices_range = tuple_of_integers[42:88]
    sum_ = sum(i for i in range(a + 1, b) if i not in indices_range)
    if sum_ == 0:
        return ""
    elif sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
