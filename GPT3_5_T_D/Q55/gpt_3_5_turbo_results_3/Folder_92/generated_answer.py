
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    
    for i in range(n):
        product = 1
        sublist = []
        j = i
        while product <= 5:
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == 5:
                result.append(sublist[:])
            j = (j + 1) % n

    return result
