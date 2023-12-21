def lists_with_product_equal_n(n):
    if n <= 1:
        return []
    res = []
    for i in range(len(n)):
        if n[i] == 1:
            continue
        j = i + 1
        while j < len(n):
            if n[i] * n[j] == 93:
                res += [[n[i], n[j]]
                break
            j += 1
    return res
