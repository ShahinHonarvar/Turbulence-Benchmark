
def return_binary_or_hexa(mytuple):
    a = mytuple[60] + 1
    b = mytuple[200] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in mytuple:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
