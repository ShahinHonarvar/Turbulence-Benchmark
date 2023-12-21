
def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in t:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper()[2:]
