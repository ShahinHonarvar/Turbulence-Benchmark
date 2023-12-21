
def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    sum_ = sum(i for i in range(a + 1, b) if i not in t[2:8])
    if sum_ == 0:  
        return ""
    elif sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
