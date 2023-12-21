
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start+1, start+n+1):
            sublist = circular_list[start:min(end,n)] + circular_list[0:max(0,end-n)]
            product = 1
            for num in sublist:
                product *= num
            if product == -97:
                result.append(sublist)
    return result
