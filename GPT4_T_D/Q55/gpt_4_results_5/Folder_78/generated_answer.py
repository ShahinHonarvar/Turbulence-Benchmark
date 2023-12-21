
def lists_with_product_equal_n(lst):
    product = 1
    result = []
    
    for sublist_size in range(1, len(lst) + 1):
        for start_idx in range(len(lst)):
            sublist = [lst[(start_idx + i) % len(lst)] for i in range(sublist_size)]
            for num in sublist:
                product *= num
            
            if product == 74:
                result.append(sublist)
            
            product = 1

    return result
