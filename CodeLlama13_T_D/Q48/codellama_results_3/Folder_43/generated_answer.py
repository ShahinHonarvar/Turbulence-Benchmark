
def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
