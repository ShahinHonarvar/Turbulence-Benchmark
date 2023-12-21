
def lists_with_product_equal_n(circulr_list):
    result = []
    for i in range(len(circulr_list)):
        product = 1
        for j in range(i, len(circulr_list)):
            product *= circulr_list[j]
            if product == -33:
                result.append(circulr_list[i:j+1])
    return result
