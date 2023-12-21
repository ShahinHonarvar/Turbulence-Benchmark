
def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[69] + 1
    b = tuple_of_ints[97] - 1
    sum_ = 0
    for i in range(a, b+1):
        if i not in tuple_of_ints:
            sum_ += i
    if sum_ % 2 == 0:
        return hex(sum_)
    else:
        return bin(sum_)
