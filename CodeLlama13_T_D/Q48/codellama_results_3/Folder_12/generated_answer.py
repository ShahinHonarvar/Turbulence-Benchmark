
def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    s = sum(x for x in range(a+1, b) if x not in t)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
