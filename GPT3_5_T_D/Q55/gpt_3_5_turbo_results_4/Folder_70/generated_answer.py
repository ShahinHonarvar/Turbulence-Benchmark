
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i+1, len(circular_list) + i + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 32:
                result.append(sublist)
    return result
