
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    arr = circular_list * 2
    for i in range(size):
        for j in range(i, i + size):
            sublist = arr[i: j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -61:
                result.append(sublist)
    return result
