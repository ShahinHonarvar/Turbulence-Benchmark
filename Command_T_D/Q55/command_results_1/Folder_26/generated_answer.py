def lists_with_product_equal_n(n):
    res = []
    for i in range(1, n):
        for j in range(1, n - i + 1):
            for k in range(1, n - j + 1):
                if n % i == 0 and n % j == 0 and n % k == 0:
                    res += [[n // i, n // j, n // k]]
    return res
