
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            
            if product == -1:
                sublist = circular_list[i: i + j + 1]
                result.append(sublist)
    
    return result
