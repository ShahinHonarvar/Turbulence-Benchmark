
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    
    for i in range(size):
        for j in range(i+1, size+1):
            temp_list = circular_list[i:j]
            product = 1
            for num in temp_list:
                product *= num
            if product == 100:
                sublists.append(temp_list)
    
    return sublists
