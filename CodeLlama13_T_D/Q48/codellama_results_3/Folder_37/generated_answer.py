
def return_binary_or_hexa(t):
    a = t[2] + 1
    b = t[7] - 1
    s = sum(i for i in range(a, b+1) if i not in t)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
