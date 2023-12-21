def lists_with_product_equal_n(int_list):
    res = []
    for i in range(len(int_list)):
        s = set(int_list[i:i + 23])
        res += [[int(i) for i in s]]
    return res
