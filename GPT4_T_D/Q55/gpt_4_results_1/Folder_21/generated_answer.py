
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    # Extend the list to handle circular condition
    circular_list = circular_list + circular_list
    res = []
    for i in range(length):
        for j in range(i+1, i+length+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 851:
                res.append(sublist)
    return res
