
def return_binary_or_hexa(tuple_):
    a = tuple_[57]
    b = tuple_[85]
    sum_ = 0
    for i in range(a+1, b-1):
        if i not in tuple_:
            sum_ += i
    return bin(sum_) if sum_ % 2 == 1 else hex(sum_)
