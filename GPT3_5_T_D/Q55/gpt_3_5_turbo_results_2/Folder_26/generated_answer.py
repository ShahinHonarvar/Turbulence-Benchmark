
def lists_with_product_equal_n(circ_list):
    result = []
    size = len(circ_list)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = circ_list[i:j] + circ_list[j:i]
            product = 1
            for num in sublist:
                product *= num
            if product == 93:
                result.append(sublist)
    return result
