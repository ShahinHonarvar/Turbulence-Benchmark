
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        j = (i+1) % len(circular_list)
        while j != i:
            product *= circular_list[j]
            if product == -91:
                result.append(sublist)
            sublist.append(circular_list[j])
            j = (j+1) % len(circular_list)
    return result
