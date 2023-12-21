
import itertools

def lists_with_product_equal_n(circular_list):
    
    length = len(circular_list)
    circular_list.extend(circular_list)
    res = []
    
    for i in range(length):
        for j in range(i+1, length+i+1):
            sub_list = circular_list[i:j]
            product = 1
            for element in sub_list:
                product *= element
                
            if product == -968:
                if sub_list not in res:
                    res.append(sub_list)
    
    return res
