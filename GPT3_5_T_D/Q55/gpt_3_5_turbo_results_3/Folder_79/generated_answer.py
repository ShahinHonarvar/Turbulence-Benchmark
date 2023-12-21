
def lists_with_product_equal_n(circle):
    n = len(circle)
    sublists = []
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = circle[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -83:
                sublists.append(sublist)
    return sublists
