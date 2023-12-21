def lists_with_product_equal_n(n):
    res = []
    for i in range(n):
        if n % i == 0:
            s = range(i, n, i)
            if n == i * i:
                res += [[s]]
            else:
                res += [[s]] + [[s + [i + 1]] + [[s + [n]]]
    return res
