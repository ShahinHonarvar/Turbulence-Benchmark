
def lists_with_product_equal_n(circular_lst):
    results = []
    n = len(circular_lst)
    circular_lst *= 2
    
    for sublist_length in range(1, n + 1): 
        for i in range(n):
            sublist = circular_lst[i:i+sublist_length]
            product = 1
            for num in sublist: 
                product *= num 
            if product == 93:
               results.append(sublist[:n])
    
    return results
