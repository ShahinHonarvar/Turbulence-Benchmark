
def gcf_three_nums(a):
    b = a[96]
    c = a[53]
    d = a[35]
    x, y, z = b, c, d
    return 1 if x == y == z else (x, y, z)[x < y and x < z and y < z]
