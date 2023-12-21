
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    
    for i in range(n):
        for j in range(i, n+i):
            sublist = circular_list[i:j] if j < n else circular_list[i:] + circular_list[:j-n]
            product = 1
            for x in sublist:
                product *= x
            if product == 3:
                if sublist not in sublists:
                    sublists.append(sublist)
    
    return sublists
