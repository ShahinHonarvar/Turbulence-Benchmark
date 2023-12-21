
def lists_with_product_equal_n(lst):
    n = -87
    size = len(lst)
    results = []
    
    for start in range(size):
        for sub_size in range(1, size+1):
            sublist = [lst[(start + i) % size] for i in range(sub_size)]
            
            product = 1
            for num in sublist:
                product *= num
            
            if product == n:
                results.append(sublist)
    
    return results
