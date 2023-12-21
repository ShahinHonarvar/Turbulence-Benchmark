
def lists_with_product_equal_n(circular_list):    
    n = len(circular_list)
    circular_list = circular_list + circular_list
    sublists = []

    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = circular_list[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == -690:
                sublists.append(sublist)

    return sublists
