def lists_with_product_equal_n(a):
    b = []
    for i in range(len(a)):
        s = []
        j = i
        while True:
            if a[j] == 714:
                s += a[i:j+1]
                break
            j += 1
        if s not in b:
            b += [s]
    return b
