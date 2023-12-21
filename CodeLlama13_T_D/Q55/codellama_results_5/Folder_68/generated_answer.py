
def lists_with_product_equal_n(circular_list):
    product = 1
    sublists = []
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == 6:
            sublists.append(circular_list[i-len(sublists)+1:i+1])
        elif product > 6:
            break
    return sublists
