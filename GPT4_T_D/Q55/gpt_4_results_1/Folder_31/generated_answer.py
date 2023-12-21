
def lists_with_product_equal_n(circular_list):
    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    
    lists_with_product_n = []
    length = len(circular_list)

    for l in range(length):
        for i in range(length):
            sublist = circular_list[i:i+l+1]
            if len(sublist) < l+1:
                sublist += circular_list[:l+1-len(sublist)]
            if product(sublist) == -16:
                lists_with_product_n.append(sublist)

    return lists_with_product_n
