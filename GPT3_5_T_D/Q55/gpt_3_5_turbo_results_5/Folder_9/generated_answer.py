
def lists_with_product_equal_n(circular_list):
    result = []
    circle = circular_list + circular_list
    size = len(circular_list)
    
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= circle[j]
            if product == -36:
                result.append(circle[i:j+1])
    
    return result
