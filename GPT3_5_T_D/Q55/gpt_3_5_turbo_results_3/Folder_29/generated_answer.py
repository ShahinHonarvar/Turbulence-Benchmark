
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i+j)%n
            product *= circular_list[index]
            if product == 15:
                sublists.append(circular_list[i:index+1])
    return sublists
