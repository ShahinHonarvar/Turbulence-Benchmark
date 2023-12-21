
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    
    for sublist_length in range(1, size + 1):
        for i in range(size):
            # Create circular sublists
            sublist = lst[i:i+sublist_length] + lst[:max(0, (i+sublist_length)-size)]
            
            # Check product equals 28
            product = 1
            for num in sublist:
                product *= num
            
            if product == 28:
                sublists.append(sublist)
    
    return sublists
