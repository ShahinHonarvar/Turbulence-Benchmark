
def lists_with_product_equal_n(circle):
    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod

    sublists = []
    for i in range(len(circle)):
        for j in range(i+1, len(circle)+1):
            sublist = circle[i:j]
            if product(sublist) == 15:
                sublists.append(sublist)

    return sublists
