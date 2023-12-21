def lists_with_product_equal_n(num_list):
    res = []
    for n in range(1, len(num_list) + 1):
        for i in range(n, 0, -1):
            p = 1
            for j in range(i, n):
                p *= num_list[j]
            if p == 5:
                res += [[num_list[i:j + 1]]
    return res
