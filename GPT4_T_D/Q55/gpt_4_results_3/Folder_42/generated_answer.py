
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)

    for sublist_size in range(1, length+1):
        for i in range(length):
            sublist = [circular_list[(i+j)%length] for j in range(sublist_size)]
            product = 1
            for num in sublist:
                product *= num
            if product == 25:
                result.append(sublist)

    return result
