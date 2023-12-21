
def lists_with_product_equal_n(lst):
    n = -94
    sublists = []
    list_len = len(lst)
    for i in range(list_len):
        for j in range(i, list_len + i):
            sublist = lst[j%list_len : (j+i)%list_len + 1]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == n:
                sublists.append(sublist)
    return [list(item) for item in set(tuple(row) for row in sublists)]
