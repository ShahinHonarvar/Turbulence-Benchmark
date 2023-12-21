
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    
    for i in range(n):
        prod = 1
        for j in range(i, i+n):
            index = j % n
            prod *= circular_list[index]
            
            if prod == 54:
                sublist = circular_list[i:index+1]
                result.append(sublist)
    
    return result
