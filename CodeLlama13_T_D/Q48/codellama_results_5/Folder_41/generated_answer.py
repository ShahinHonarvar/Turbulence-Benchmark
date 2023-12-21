
def return_binary_or_hexa(mytuple):
    a = mytuple[3] + 1
    b = mytuple[8] - 1
    sum = 0
    for i in range(a, b+1):
        if not (i in mytuple[3:9]):
            sum += i
    if (sum % 2) == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper()[2:]
