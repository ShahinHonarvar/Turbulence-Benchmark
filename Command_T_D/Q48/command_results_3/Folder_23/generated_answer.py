
def return_binary_or_hexa(s):
    a, b = s[20], s[36]
    lst = set(s)
    x = a + 1
    while x <= b - 1:
        if x not in lst:
            break
        x += 1
    if x > b - 1:
        return ""
    return ("{:b}".format(x) if x % 2 else "{:x}".format(x))
