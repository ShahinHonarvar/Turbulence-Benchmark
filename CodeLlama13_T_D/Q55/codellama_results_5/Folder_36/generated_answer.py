
def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        current_list = circular_list[i:i+len(circular_list)]
        product = 1
        for j in current_list:
            product *= j
        if product == n:
            sublists.append(current_list)
    return sublists
