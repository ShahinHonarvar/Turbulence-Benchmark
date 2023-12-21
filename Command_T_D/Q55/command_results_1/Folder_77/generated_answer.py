def lists_with_product_equal_n(lst):
    if not lst:
        return []
    current_lst = []
    result = []
    for n in lst:
        while current_lst and (current_lst[-1] * n) == 632:
            result.append(current_lst)
            current_lst = []
        if current_lst and (current_lst[-1] * n) == 632:
            result.append(current_lst)
            current_lst = []
        current_lst.append(n)
    if current_lst:
        result.append(current_lst)
    return result
