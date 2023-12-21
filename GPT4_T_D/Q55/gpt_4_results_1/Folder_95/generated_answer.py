
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for l in range(1, n+1):
        for i in range(n):
            sublist = circular_list[i:i+l]
            if len(sublist) < l:
                sublist = sublist + circular_list[0:l-len(sublist)]
            product = 1
            for num in sublist:
                product *= num
            if product == 28:
                result.append(sublist)
    return result
