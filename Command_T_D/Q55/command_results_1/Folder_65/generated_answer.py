def lists_with_product_equal_n(a_list):
    res = []
    for i in range(len(a_list)):
        for j in range(i + 1, len(a_list)):
            if a_list[i] * a_list[j] == 46:
                res.append(a_list[i:j+1])
    return res
