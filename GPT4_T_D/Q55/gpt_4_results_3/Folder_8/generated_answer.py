
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)

    for start in range(n):
        for end in range(start+1, n+1):
            sublist = circular_list[start:end]
            if end == n:
                sublist += circular_list[:start]
            
            product = 1
            for num in sublist:
                product *= num
            
            if product == -41:
                sublists.append(sublist)
            
    return sublists
