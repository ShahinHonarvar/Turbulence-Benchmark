
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list += circular_list[:n-1]  
    prod_list = []

    for v in range(n):
        for w in range(v+1, v+n):
            sublist = circular_list[v:w]
            product = 1
            for x in sublist:
                product *= x
            if product == 43:
                prod_list.append(sublist)

    return prod_list
