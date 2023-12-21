
def lists_with_product_equal_n(circle_list):
    sublists = []
    for i in range(len(circle_list)):
        product = 1
        for j in range(i, len(circle_list)):
            product *= circle_list[j]
            if product == 0:
                sublists.append(circle_list[i:j+1])
    return sublists
