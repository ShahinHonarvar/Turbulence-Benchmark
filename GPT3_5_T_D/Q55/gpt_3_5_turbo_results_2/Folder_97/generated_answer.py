
def lists_with_product_equal_n(lst):
    def product(sublst):
        prod = 1
        for num in sublst:
            prod *= num
        return prod

    sublists = []
    n = len(lst)
    product_n = -938

    for start in range(n):
        for end in range(start, start + n):
            sublist = lst[start:end+1]
            if product(sublist) == product_n:
                sublists.append(sublist)
    
    return sublists
