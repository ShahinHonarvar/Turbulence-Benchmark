
def lists_with_product_equal_n(circular_list):
    out = []
    n = len(circular_list)
    circular_list = circular_list + circular_list

    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 10:
                out.append(sublist)
    
    return out
