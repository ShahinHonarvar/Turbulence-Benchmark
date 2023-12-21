
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    sum_ = sum(set(range(a + 1, b)) - set(numbers[57:86]))
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
