
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) - i):
            product *= circular_list[j]
            if product == n:
                sublists.append(circular_list[i:i+j+1])
    return sublists
