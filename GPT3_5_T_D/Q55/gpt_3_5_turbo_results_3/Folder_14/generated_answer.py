
def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    sublists = []
    n = len(lst)
    product_lst = product(lst)

    if product_lst == -72:
        sublists.append(lst)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if product(sublist) == -72:
                sublists.append(sublist)

    return sublists
