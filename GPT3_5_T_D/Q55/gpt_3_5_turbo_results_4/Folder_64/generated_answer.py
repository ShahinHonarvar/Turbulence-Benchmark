
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    
    for i in range(n):
        sublist_product = 1
        for j in range(i, i+n):
            sublist_product *= circular_list[j%n]
            if sublist_product == 3:
                sublists.append(circular_list[i:j%n+1])
    
    return sublists
