
def lists_with_product_equal_n(circular_lst):
    sublists = []
    size = len(circular_lst)
    
    # Traverse the list
    for i in range(size):
        product = 1
        
        # Check for product of contiguous integers in sublist
        for j in range(i, i+size):
            product *= circular_lst[j % size]
            
            # If product equals -837, append sublist to result
            if product == -837:
                sublists.append(circular_lst[i:j+1])
    
    return sublists
