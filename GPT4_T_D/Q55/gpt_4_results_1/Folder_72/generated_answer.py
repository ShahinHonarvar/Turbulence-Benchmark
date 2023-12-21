
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    circular_list = circular_list + circular_list
    for length in range(1, n+1):
        for i in range(n):
            sublist = circular_list[i:i+length]
            product = 1
            for num in sublist:
                product *= num
            if product == 10:
                sublists.append(sublist)
    return sublists
