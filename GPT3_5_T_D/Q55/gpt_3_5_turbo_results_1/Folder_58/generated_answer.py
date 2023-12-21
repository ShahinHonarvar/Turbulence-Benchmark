
def lists_with_product_equal_n(circular_list):
    result = []
    product = 1
    
    for i in range(len(circular_list)):
        product *= circular_list[i]
        
        if product == 733:
            result.append(circular_list[:i+1])
            
        elif product > 733:
            while product > 733:
                product /= circular_list[0]
                circular_list = circular_list[1:]
                
                if product == 733:
                    result.append(circular_list)                  
                    
    return result
