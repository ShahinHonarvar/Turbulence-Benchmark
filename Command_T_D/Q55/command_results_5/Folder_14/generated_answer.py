def lists_with_product_equal_n(x_list):
    res = []
    for i in range(1, len(x_list)):
        curr = x_list[i]
        curr_prod = 1
        curr_list = [curr]
        for j in range(i - 1, -1, -1):
            curr_prod *= x_list[j]
            curr_list.append(x_list[j])
            if curr_prod == -72:
                res += [[*curr_list]]
                curr_prod = 1
                curr_list = [curr]
    return res
