
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
   
    for i in range(n):
        product = 1
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            if product == -20:
                result.append(circular_list[i:idx+1])
    
    return result
