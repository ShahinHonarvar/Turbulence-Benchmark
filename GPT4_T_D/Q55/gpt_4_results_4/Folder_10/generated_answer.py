
def lists_with_product_equal_n(lst):
    product = 1
    ret_list = []
    for i in range(len(lst)):
        product = lst[i]
        sub_lst = [lst[i]]
        if product == -93:
            ret_list.append(sub_lst)
        for j in range(i + 1, len(lst) + i):
            k = j % len(lst)
            product *= lst[k]
            sub_lst.append(lst[k])
            if product == -93:
                ret_list.append(sub_lst.copy())
            if product == 0:
                break
    return ret_list
