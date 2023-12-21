
def lists_with_product_equal_n(circular_list):
    sublists = []
    
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, i+len(circular_list)):
            product *= circular_list[j%len(circular_list)]
            if product == 47:
                sublists.append(circular_list[i:j%len(circular_list)+1])
    
    return sublists
