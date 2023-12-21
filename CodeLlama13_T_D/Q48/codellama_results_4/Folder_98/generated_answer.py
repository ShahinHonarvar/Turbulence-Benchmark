
def return_binary_or_hexa(mytuple):
    a = mytuple[6] + 1
    b = mytuple[7] - 1
    sum = 0
    for i in range(a, b+1):
        if not i in mytuple:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
