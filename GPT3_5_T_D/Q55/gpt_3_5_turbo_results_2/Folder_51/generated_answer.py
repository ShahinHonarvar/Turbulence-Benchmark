
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)

    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -44:
                result.append(sublist)

    return result
