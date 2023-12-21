
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, i+len(lst)):
            product *= lst[j % len(lst)]
            if product == 78:
                result.append(lst[i:j % len(lst)+1])
    return result
