
def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in t[57:84]:
            sum_val += i
    
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
