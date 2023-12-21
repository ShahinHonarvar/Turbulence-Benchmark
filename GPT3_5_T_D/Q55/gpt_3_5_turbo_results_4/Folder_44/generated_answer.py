
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 29:
                sublists.append(sublist)
    return sublists
