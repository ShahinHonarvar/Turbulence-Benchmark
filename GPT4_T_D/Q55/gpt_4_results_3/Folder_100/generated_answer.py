
def lists_with_product_equal_n(circular_list):
    n = 48
    sublists = []
    size = len(circular_list)
    
    for i in range(size):
        for j in range(i+1, size+1):
            product = 1
            for element in circular_list[i:j]:
                product *= element
            if product == n:
                sublists.append(circular_list[i:j])
    
    return sublists
