def lists_with_product_equal_n(int_list):
    result = []
    for a in range(1, len(int_list)):
        for b in range(a, len(int_list)):
            for c in range(b, len(int_list)):
                if int_list[a] * int_list[b] * int_list[c] == -10:
                    result.append([int_list[a], int_list[b], int_list[c]])
    return result
