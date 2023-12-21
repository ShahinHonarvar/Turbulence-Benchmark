
def return_binary_or_hexa(test_tup):
    a, b = test_tup[57], test_tup[85]
    sum_ = a + 1
    while sum_ < b:
        if sum_ not in test_tup:
            break
        sum_ += 1
    if sum_ % 2:
        return format(sum_, 'b')
    return format(sum_, 'x')
