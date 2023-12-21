
def lists_with_product_equal_n(lst):
    n = len(lst)
    prods = []
    for i in range(n):
        for j in range(i+1, n+1):
            sub_lst = lst[i:j] + lst[:i] + lst[j:]
            prod = 1
            for num in sub_lst:
                prod *= num
            if prod == -26:
                prods.append(sub_lst)
    return prods
