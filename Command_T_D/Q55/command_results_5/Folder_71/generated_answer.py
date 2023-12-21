def lists_with_product_equal_n(n):
    lists = []
    for i in range(1, n // 2):
        for j in range(i + 1, n // 2):
            p = 1
            while p <= n:
                if p == i:
                    break
                elif p == j:
                    break
                p *= i + j
            if p == 47:
                lists.append([i, j])
    return lists
