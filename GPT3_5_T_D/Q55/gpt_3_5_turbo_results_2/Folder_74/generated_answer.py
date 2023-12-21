
def lists_with_product_equal_n(lst):
    def product_of_sublist(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product

    product = 51
    result = []

    length = len(lst)
    for i in range(length):
        for j in range(i, length):
            sublist = lst[i:j+1]
            if product_of_sublist(sublist) == product:
                result.append(sublist)

    return result
