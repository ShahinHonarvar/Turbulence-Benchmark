
def return_binary_or_hexa(mytuple):
    a = mytuple[54]
    b = mytuple[83]
    s = sum(i for i in range(a + 1, b) if i not in mytuple)
    if s % 2 == 0:
        return format(s, 'x')
    else:
        return bin(s)[2:]
