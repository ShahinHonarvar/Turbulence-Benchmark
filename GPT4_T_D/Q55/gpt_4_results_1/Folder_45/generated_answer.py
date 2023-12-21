
def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    
    for window_size in range(1, size+1):
        for i in range(size):
            product = 1
            temp = []
            for j in range(i, i + window_size):
                product *= lst[j % size]
                temp.append(lst[j % size])
                
                if product == -5:
                    result.append(temp.copy())
                    break
                
    return result
