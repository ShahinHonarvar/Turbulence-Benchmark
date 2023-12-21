
def lists_with_product_equal_n(circ_list):
    def product_equals_n(sublist):
        prod = 1
        for i in sublist:
            prod *= i
        return prod == -41
    
    size = len(circ_list)
    circ_list += circ_list
    result = []
    for i in range(size):
        for j in range(1, size + 1):
            sublist = circ_list[i:i+j]
            if product_equals_n(sublist):
                result.append(sublist)
    return result
