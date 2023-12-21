
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    circular_list += circular_list
    res = []
    
    for l in range(1, length + 1):
        for i in range(length):
            sublist = circular_list[i:i+l]
            product = 1
            for x in sublist:
                product *= x
            if product == 29:
                res.append(sublist[:length])

    return res
