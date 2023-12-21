
def lists_with_product_equal_n(circular_list):
    res = []
    num_len = len(circular_list)
    for i in range(num_len):
        for t in range(1, num_len+1):  
            tmp = []
            
            for j in range(i,i+t):  
                j = j%num_len  
                tmp.append(circular_list[j]) 
                
            product_of_elements = 1
            for el in tmp:
                product_of_elements *= el
                
            if product_of_elements == -76:
                res.append(tmp)
    return res
