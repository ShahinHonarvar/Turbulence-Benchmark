
def lists_with_product_equal_n(lst):
    def product(sublst):
        result = 1
        for num in sublst:
            result *= num
        return result

    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            sublst = lst[i:j+1] + lst[:j+1]
            if product(sublst) == -72:
                sublists.append(sublst)

    return sublists
