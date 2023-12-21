
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -7:
                sublists.append(sublist)
    return sublists
