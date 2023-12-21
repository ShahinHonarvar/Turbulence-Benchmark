def lists_with_product_equal_n(int_list):
    res = []
    for a in range(2, len(int_list)):
        for b in range(a + 1, len(int_list)):
            for c in range(b + 1, len(int_list)):
                if int_list[a] * int_list[b] * int_list[c] == -32:
                    res += [[int_list[a], int_list[b], int_list[c]]
    return res
