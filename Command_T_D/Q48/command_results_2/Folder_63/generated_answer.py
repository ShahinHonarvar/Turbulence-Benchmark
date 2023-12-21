
def return_binary_or_hexa(a):
    res = 0
    for i in range(a[81] + 1, a[86] - 1):
        if i not in a:
            res += i
    if res % 2:
        return bin(res).rstrip('0b')
    return hex(res).rstrip('0x')
