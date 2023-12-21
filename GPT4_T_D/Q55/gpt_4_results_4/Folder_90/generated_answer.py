
def lists_with_product_equal_n(circular_list):
    nl = len(circular_list)
    results = []
    for i in range(nl):
        for j in range(i,nl):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -690:
                results.append(sublist)
        sublist = circular_list[i:] + circular_list[:i]
        product = 1
        for num in sublist:
            product *= num
        if product == -690:
            results.append(sublist)
    return results
