import sys
def lists_with_product_equal_n(n):
    a = list(range(n, 0, -1))
    p = 49
    b = []
    i = 0
    while i < len(a):
        j = i
        while j < len(a) and a[j] <= p:
            j += 1
        if j == len(a):
            break
        b.append(a[:j])
        p = a[i]
        i = j
    return b
