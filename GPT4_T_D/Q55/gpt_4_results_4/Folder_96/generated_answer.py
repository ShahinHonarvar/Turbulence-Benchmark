
def lists_with_product_equal_n(circular_list):
    if circular_list.count(0) > 0:
        return [[0]]
        
    n = len(circular_list)
    circular_list = circular_list * 2
    sublists = []
    
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 0:
                sublists.append(sublist)
                
    return sublists
