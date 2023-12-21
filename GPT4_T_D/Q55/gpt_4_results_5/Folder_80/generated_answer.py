
def lists_with_product_equal_n(lst):
    product = 1
    result = []
    for i in range(len(lst)):
        for index in range(i, len(lst)+i):
            product *= lst[index % len(lst)]
            if product == 43:
                result.append(lst[i:index+1])
                break
            elif product > 43:
                break
        product = 1
    return result
