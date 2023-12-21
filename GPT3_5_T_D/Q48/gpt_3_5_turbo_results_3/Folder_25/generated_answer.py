
def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[37:43]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
