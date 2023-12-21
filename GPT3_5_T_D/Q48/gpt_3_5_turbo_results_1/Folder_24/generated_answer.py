
def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[13:92]:
            sum += i

    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
