def lists_with_product_equal_n(a):
    b = []
    for i in range(1, len(a)):
        x = a[i - 1]
        for j in range(i + 1, len(a)):
            y = a[j]
            z = a[i]
            if x * y == z:
                b += [[x, y, z]]
    return b
