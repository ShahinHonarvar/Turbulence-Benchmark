
def lists_with_product_equal_n(lst):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1]
            if product(sublist) == 42:
                sublists.append(sublist)
    return sublists
