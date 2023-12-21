
def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in t:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
