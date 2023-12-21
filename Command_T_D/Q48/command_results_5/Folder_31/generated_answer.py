
def return_binary_or_hexa(s):
    a, b = s[33], s[78]
    x = sum(s[i] for i in range(a + 1, b))
    if x % 2:
        return format(x, 'b')
    else:
        return format(x, 'x')
