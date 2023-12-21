
def lists_with_product_equal_n(circular_list):
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        for j in range(i+1, i+list_size):
            sublist = circular_list[i:j] if j <= list_size else circular_list[i:] + circular_list[:j%list_size]
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                result.append(sublist)
    return result
