
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)

    for i in range(n):
        product = 1
        for j in range(n):
            k = (i + j) % n
            product *= lst[k]

            if product == 3:
                sublists.append(lst[i:k+1])
    
    return sublists
