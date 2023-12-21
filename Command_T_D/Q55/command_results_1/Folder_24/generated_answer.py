def lists_with_product_equal_n(num_list):
    res = []
    i = 0
    while i < len(num_list):
        curr_list = []
        curr_list.append(num_list[i])
        curr_prod = 1
        curr_idx = i
        while curr_idx != -1:
            curr_prod *= num_list[curr_idx]
            curr_idx = curr_idx.next_idx()
            curr_list.append(num_list[curr_idx])
            if curr_prod == -89:
                res.append(curr_list)
                break
        i += 1
    return res
