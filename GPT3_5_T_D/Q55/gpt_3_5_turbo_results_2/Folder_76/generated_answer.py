
def lists_with_product_equal_n(circular_list):
    lst = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == 247:
                lst.append(circular_list[i:i+j+1])
    return lst
