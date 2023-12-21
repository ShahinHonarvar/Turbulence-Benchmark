
def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    sum_ = 0
    for num in range(a + 1, b):
        if num not in t[21:37]:
            sum_ += num
    if sum_ == 0:
        return ''
    elif sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]
