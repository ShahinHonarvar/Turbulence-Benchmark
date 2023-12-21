
def return_binary_or_hexa(lst):
    i = 60
    j = 90
    res = 0
    while i < j:
        res += lst[i]
        i += 1
    if res % 2 == 1:
        return bin(res)[2:]
    return hex(res)[2:]
