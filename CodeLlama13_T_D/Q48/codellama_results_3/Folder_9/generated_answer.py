
def return_binary_or_hexa(mytuple):
    a = mytuple[70] + 1
    b = mytuple[200] - 1
    result = sum(x for x in range(a, b+1) if x not in mytuple)
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]
