
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        temp = []
        for j in range(i, len(lst)):
            product *= lst[j]
            temp.append(lst[j])
            if product == n:
                result.append(temp)
    return result
