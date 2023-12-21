
def lists_with_product_equal_n(lst):
    def product(sublst):
        result = 1
        for num in sublst:
            result *= num
        return result

    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublst = lst[i:j+1]
            if product(sublst) == 28:
                sublists.append(sublst)

    return sublists
