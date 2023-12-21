
def lists_with_product_equal_n(lst):
    out = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst) + 1):
            sublist = lst[i:j]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == 4:
                out.append(sublist)
    return out
