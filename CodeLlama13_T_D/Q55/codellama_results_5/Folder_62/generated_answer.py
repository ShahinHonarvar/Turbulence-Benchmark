
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+len(circular_list)]
        product = 1
        for num in sublist:
            product *= num
        if product == 100:
            result.append(sublist)
    return result
