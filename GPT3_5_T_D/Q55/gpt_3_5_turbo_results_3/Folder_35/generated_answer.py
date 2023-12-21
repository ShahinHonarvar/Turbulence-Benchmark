
def lists_with_product_equal_n(lst):
    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod

    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j]
            if product(sublist) == 83:
                sublists.append(sublist)
    return sublists
