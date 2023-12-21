
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, i + len(lst)):
            product *= lst[j % len(lst)]
            if product == -57:
                sub_list = lst[i:j+1]
                result.append(sub_list)
    return result
