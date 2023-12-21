
def return_binary_or_hexa(a):
    b = a[8]
    res = sum(i for i in range(a[1] + 1, b - 1) if i not in a)
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
