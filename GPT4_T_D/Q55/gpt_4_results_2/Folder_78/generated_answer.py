
def lists_with_product_equal_n(lst):
    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p

    sublists = []
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i+1, len_lst+1):
            lst_ij = lst[i:j]
            if product(lst_ij) == 74:
                sublists.append(lst_ij)
        lst.append(lst.pop(0))
    return sublists
