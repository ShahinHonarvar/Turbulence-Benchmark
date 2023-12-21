
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)

    for i in range(n):
        product = lst[i]

        if product == -9:
            sublists.append(lst[i:i+1])

        for j in range(i+1, n):
            product *= lst[j]

            if product == -9:
                sublists.append(lst[i:j+1])

    return sublists
