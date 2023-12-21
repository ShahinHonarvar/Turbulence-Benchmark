
def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+len(result)]
        if len(sublist) <= len(circular_list):
            product = 1
            for j in sublist:
                product *= j
            if product == n:
                result.append(sublist)
    return result
