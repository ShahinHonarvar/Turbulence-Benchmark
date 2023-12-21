
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        prod = 1
        for j in range(i, i+n):
            prod *= lst[j%n]
            if prod > 91:
                break
            elif prod == 91:
                sublists.append(lst[i:j+1])
    return sublists
