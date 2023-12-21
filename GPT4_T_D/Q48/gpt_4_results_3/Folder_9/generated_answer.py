
def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    sum_ = sum(set(range(a+1, b)) - set(t[70:201]))
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    elif sum_ != 0:
        return hex(sum_)[2:]
    else:
        return ''
