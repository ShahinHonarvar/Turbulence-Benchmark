def lists_with_product_equal_n(n):
    lists = []
    for i in range(len(n) // 2):
        if n[i] * n[i + len(n) // 2] == 2:
            lists.append(list(range(i, i + len(n) // 2)))
    return lists
