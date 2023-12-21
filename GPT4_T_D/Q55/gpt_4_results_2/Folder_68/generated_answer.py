
def lists_with_product_equal_n(lst):
    all_sublists = []

    n = len(lst)
    lst_extended = lst*2

    for start in range(n):
        for l in range(1, n + 1):
            sublist = lst_extended[start : start + l]
            product = 1
            for item in sublist:
                product *= item
            if product == 6:
                all_sublists.append(sublist)

    return all_sublists
