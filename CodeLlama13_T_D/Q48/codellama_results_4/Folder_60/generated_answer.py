
def return_binary_or_hexa(mytuple):
    a, b = mytuple[38], mytuple[52]
    result = 0
    for i in range(a + 1, b - 1 + 1):
        if i not in mytuple:
            result += i
    if result % 2 == 0:
        return hex(result)
    else:
        return bin(result)[2:]
