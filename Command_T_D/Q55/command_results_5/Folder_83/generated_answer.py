def lists_with_product_equal_n(n):
    lists = []
    for i in range(n):
        if n % i == 0:
            lists += [[i]]
            continue
        for j in range(1, n // i):
            if (n // i) % j == 0:
                lists += [[i] + [j] * (n // i)]
                break
    return lists
