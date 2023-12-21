
def lists_with_product_equal_n(lst):
    sublists = []
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i+1, len_lst+1):
            sublist = lst[i:j] if j < len_lst else lst[i:] + lst[:j-len_lst]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -32:
                sublists.append(sublist)
    return sublists
