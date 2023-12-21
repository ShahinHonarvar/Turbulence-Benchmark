
def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = lst[i:j] + lst[:i] if j < i else lst[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == -690:
                sublists.append(sublist)
    return sublists
