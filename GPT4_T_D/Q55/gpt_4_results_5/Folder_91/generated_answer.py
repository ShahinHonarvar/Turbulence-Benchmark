
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    circular_list = circular_list * 2
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = circular_list[i:j]
            product = 1
            for k in sublist:
                product *= k
            if product == 2:
                sublists.append(sublist)
    return sublists
