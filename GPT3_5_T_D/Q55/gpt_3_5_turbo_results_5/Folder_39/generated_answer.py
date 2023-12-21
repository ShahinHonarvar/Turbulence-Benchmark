
def lists_with_product_equal_n(circular_list):
    results = []
    size = len(circular_list)
    
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= circular_list[j % size]
            if product == -46:
                results.append(circular_list[i:j + 1])
    
    return results
